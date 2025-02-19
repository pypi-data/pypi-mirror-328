#!/usr/bin/python
import re
from dataclasses import dataclass
from collections import defaultdict
from .utils import (
    listify,
    DictQueue,
    splitter,
    infinitely_many_of,
    intersperse,
    flatten,
    plus,
    INFINITY,
)
from functools import reduce
import argparse
import sys
import os

global DEBUG
DEBUG = False

arg_parser = argparse.ArgumentParser(prog="Gothic, v0.0.1")
arg_parser.add_argument(
    "exprs",
    help="Gothic program expressions.",
    type=str,
    nargs=argparse.REMAINDER,
    default=[],
)
arg_parser.add_argument(
    "-f",
    "--file",
    help="Path to program src file.",
    type=str,
    default=None,
)
arg_parser.add_argument(
    "-v",
    "--verbose",
    help="Print the expression encountered at each step of execution.",
    action="store_true",
)
arg_parser.add_argument(
    "--varchar",
    help="Char used to denote Variable tokens. | Singular -- [<var_name>]<char>[<regex>] | Plural -- [<var_name>]<char><char>[<regex>] | default: '",
    type=str,
    default="'",
)
arg_parser.add_argument(
    "--wildchar",
    help="Char used by Wildcard tokens. | Singular -- <char> | Plural -- <char><char> | default: .",
    type=str,
    default=".",
)
arg_parser.add_argument(
    "--rightarrow",
    help="Right-arrow token. default: =>",
    type=str,
    default="=>",
)
arg_parser.add_argument(
    "--end",
    help="End token. default: ;",
    type=str,
    default=";",
)
arg_parser.add_argument(
    "--interp_stdin_rules",
    help="Enable interpretion of any rewrite-rules present in stdin. WARNING: Security Risk from malicious rule-injection.",
    action="store_true",
)
args = arg_parser.parse_args()
args.varchar = re.escape(args.varchar)
args.wildchar = re.escape(args.wildchar)
args.rightarrow = re.escape(args.rightarrow)
args.end = re.escape(args.end)

arg_validator = {
    "exprs": lambda _: True,
    "file": lambda _: True,
    "verbose": lambda _: True,
    "interp_stdin_rules": lambda _: True,
    "varchar": lambda v: re.fullmatch(r"\\?\S", v) and v != args.wildchar,
    "wildchar": lambda w: re.fullmatch(r"\\?\S", w) and w != args.varchar,
    "rightarrow": lambda e: re.fullmatch(r"\S+", e)
    and e
    not in [
        args.varchar,
        args.varchar * 2,
        args.wildchar,
        args.wildchar * 2,
        args.end,
    ],
    "end": lambda e: re.fullmatch(r"\S+", e)
    and e
    not in [
        args.varchar,
        args.varchar * 2,
        args.wildchar,
        args.wildchar * 2,
        args.rightarrow,
    ],
}
for arg, val in vars(args).items():
    validator = arg_validator[arg]
    try:
        assert validator(val)
    except:
        raise ValueError(f"Argument {arg} had invalid value: {val}")

global LOG
VERBOSE = args.verbose

global INTERP_STDIN_RULES
INTERP_STDIN_RULES = args.interp_stdin_rules


class Token:
    syntax = None
    default = None
    paraheterogenous_match = False

    def __init__(self, S: str = None):
        S = self.default if S is None else S
        if not re.fullmatch(self.syntax, S):
            raise SyntaxError(
                f"String {S} fails to match syntax regex {self.syntax} for token type {type(self)}"
            )
        self.val = S
        for k, v in re.search(self.syntax, S).groupdict().items():
            setattr(self, k, v)

    def __eq__(self, other):
        return self.val == other.val

    def __hash__(self):
        return hash(self.val)

    def __repr__(self):
        return self.val

    def __str__(self):
        return self.val


class Variable(Token):
    syntax = (
        r"(?P<name>.*?)(?P<var_marker>"
        + args.varchar
        + r"{1,2})(?P<match_flag>[!]?)(?P<regex>.*)"
    )

    def __init__(self, S: str):
        super().__init__(S)
        if self.regex == "":
            self.regex = r".+"

    @property
    def singular(self):
        return len(self.var_marker) == 1

    @property
    def plural(self):
        return not self.singular

    def matches(self, other: Token):
        match self.match_flag:
            case "!":
                return not re.fullmatch(self.regex, other.val)
            case _:
                return re.fullmatch(self.regex, other.val)


class Wildcard(Token):
    syntax = rf"{args.wildchar}{args.wildchar}?"
    paraheterogenous_match = True

    @property
    def singular(self):
        return len(self.val) == 1

    @property
    def plural(self):
        return not self.singular


class RightArrow(Token):
    syntax = rf"{args.rightarrow}(?P<second_arrowhead>[{args.rightarrow[-1]}])?"
    default = args.rightarrow

    @property
    def singular(self):
        return self.second_arrowhead is None

    @property
    def plural(self):
        return not self.singular


class End(Token):
    syntax = rf"{args.end}"
    default = args.end


TOKEN_TYPES = [Variable, Wildcard, RightArrow, End]


class Literal(Token):
    syntax = r"(?!" + "|".join(f"({t.syntax})" for t in TOKEN_TYPES) + ").+"


TOKEN_TYPES += [Literal]


def lex(S: str):
    tokens = []
    for s in re.split(r"\s+", S.strip()):
        for T in TOKEN_TYPES:
            try:
                token = T(s)
                tokens += [token]
                break
            except SyntaxError as e:
                if DEBUG:
                    print(e)
                continue
    return tokens


# {Token : list[Pattern]}
class MatchMap:
    def __init__(self, mapping={}):
        self.mapping = defaultdict(
            list,
            {
                k: listify(Pattern(v) if isinstance(v, Token) else v)
                for k, v in mapping.items()
            },
        )

    def __getitem__(self, k):
        return self.mapping[k]

    def __contains__(self, k):
        return len(self.mapping[k]) > 0

    def __add__(self, other):
        if other is None:
            return None
        combined_mapping = defaultdict(list, {k: v for k, v in self.mapping.items()})
        for k, v in other.mapping.items():
            combined_mapping[k] += v
        return MatchMap(combined_mapping)

    def __len__(self):
        """
        length of the target pattern matched
        """
        return sum(sum(len(p) for p in self.mapping[k]) for k in self.mapping)

    def __repr__(self):
        return str(self.mapping)

    @property
    def criteria(self):
        return Pattern(*[k for k in self.mapping])

    @property
    def target(self):
        return reduce(plus, flatten([v for k, v in self.mapping.items()]))

    def rewrite(self, pattern):
        if len(pattern) == 0:
            return Pattern()
        # you know youre fuckin GOONIN when your code
        rewrite_map = DictQueue(  # 1) invents a chimeric data structure
            {
                token: (
                    infinitely_many_of(
                        replacement_patterns[0]
                    )  # 2) uses infinitely many of the same god damn thing
                    if not token.paraheterogenous_match  # 3) adds an entirely new word to the English language
                    else replacement_patterns
                )
                for token, replacement_patterns in self.mapping.items()
            }
        )
        return reduce(
            lambda l, r: l + r,
            (rewrite_map[t] if t in rewrite_map else Pattern(t) for t in pattern),
        )


class Pattern:
    def __init__(self, *tokens: Token):
        assert all(isinstance(t, Token) for t in tokens)
        self.tokens = tokens

    @classmethod
    def lex(cls, src: str):
        return cls(*lex(src))

    def __getitem__(self, k):
        if isinstance(k, slice):
            indices = range(*k.indices(len(self.tokens)))
            return Pattern(*[self.tokens[i] for i in indices])
        return self.tokens[k]

    def __eq__(self, other):
        return self.tokens == other.tokens

    def __iter__(self):
        for t in self.tokens:
            yield t

    def __contains__(self, K):
        if isinstance(K, Token):
            return K in self.tokens
        if type(K) is Pattern:
            return any(t in self.tokens for t in K)
        return False

    def __add__(self, other):
        return Pattern(*(self.tokens + other.tokens))

    def __len__(self):
        return len(self.tokens)

    def __repr__(self):
        return " ".join(map(str, self.tokens))

    def matches_in(criteria_pattern, target_pattern):
        return bool(criteria_pattern.find_match_in(target_pattern))

    def find_match_in(criteria_pattern, target_pattern, keep_remainder=False):
        for i in range(len(target_pattern)):
            match = criteria_pattern.matches_beginning(target_pattern[i:])
            if match:
                return (
                    match
                    if not keep_remainder
                    else (match, target_pattern[:i], target_pattern[i + len(match) :])
                )
        return None if not keep_remainder else (None, target_pattern, Pattern())

    def matches_beginning(
        criteria_pattern, target_pattern, match_vars={}
    ) -> MatchMap | None:
        if len(criteria_pattern) == 0:  # Nothingness is present in Everything
            return MatchMap()
        if (
            len(criteria_pattern) != 0 and len(target_pattern) == 0
        ):  # Somethingness cannot match Nothingness
            return None

        criteria_token = criteria_pattern[0]
        target_token = target_pattern[0]

        match criteria_token:
            case Variable(singular=True):
                if not criteria_token.matches(target_token):
                    return None
                if (
                    criteria_token in match_vars
                    and not match_vars[criteria_token] == target_token
                ):
                    return None
                var_mapping = {criteria_token: target_token}
                return MatchMap(var_mapping) + criteria_pattern[1:].matches_beginning(
                    target_pattern[1:], {**match_vars, **var_mapping}
                )

            case Variable(plural=True):
                for i in reversed(range(len(target_pattern))):
                    if not all(
                        criteria_token.matches(t) for t in target_pattern[: i + 1]
                    ):
                        continue
                    if (
                        criteria_token in match_vars
                        and match_vars[criteria_token] != target_pattern[: i + 1]
                    ):
                        continue
                    vars_mapping = {criteria_token: target_pattern[: i + 1]}
                    matched = MatchMap(vars_mapping) + criteria_pattern[
                        1:
                    ].matches_beginning(
                        target_pattern[i + 1 :], {**match_vars, **vars_mapping}
                    )
                    if matched:
                        return matched
                return None

            case Wildcard(singular=True):
                return MatchMap({criteria_token: target_token}) + criteria_pattern[
                    1:
                ].matches_beginning(target_pattern[1:], match_vars)

            case Wildcard(plural=True):
                for i in reversed(range(len(target_pattern))):
                    matched = MatchMap(
                        {criteria_token: target_pattern[: i + 1]}
                    ) + criteria_pattern[1:].matches_beginning(
                        target_pattern[i + 1 :], match_vars
                    )
                    if matched:
                        return matched
                return None

            case Token():
                if not criteria_token == target_token:
                    return None
                return MatchMap({criteria_token: target_token}) + criteria_pattern[
                    1:
                ].matches_beginning(target_pattern[1:], match_vars)

            case _:
                raise Exception(
                    f"Undefined behavior encountered during matches_beginning w/ args: criteria_token {criteria_token} target_token {target_token} criteria_pattern {criteria_pattern} target_pattern {target_pattern} match_vars {match_vars}"
                )


# PATTERN CONSTANTS
SINGULAR_RIGHT_ARROW = Pattern(RightArrow())
PLURAL_RIGHT_ARROW = Pattern(RightArrow(args.rightarrow + args.rightarrow[-1]))
END = Pattern(End())


class Rule:
    def __init__(self, lhs: Pattern, rightarrow: RightArrow, rhs: Pattern):
        self.lhs = lhs
        self.rightarrow = rightarrow
        self.rhs = rhs

    @property
    def max_rewrites_per_line(self):
        return 1 if self.rightarrow.singular else INFINITY

    def __repr__(self):
        return f"lhs: {self.lhs} rightarrow: {self.rightarrow} rhs: {self.rhs}"

    def is_applicable(self, pattern: Pattern) -> bool:
        return self.lhs.matches_in(pattern)

    def apply(self, pattern: Pattern) -> Pattern:
        match_map, left_remainder, right_remainder = self.lhs.find_match_in(
            pattern, keep_remainder=True
        )
        rewritten_middle = (
            match_map.rewrite(self.rhs) if match_map is not None else Pattern()
        )
        return left_remainder + rewritten_middle + right_remainder


def parse_rules(expr: Pattern) -> [Rule]:
    rules = []
    all_lhs = []
    while True:
        is_rule, lhs_part, rhs = SINGULAR_RIGHT_ARROW.find_match_in(
            expr, keep_remainder=True
        )
        if not is_rule:
            break
        all_lhs += [lhs_part]
        lhs = reduce(lambda l, r: l + r, intersperse(SINGULAR_RIGHT_ARROW, all_lhs))
        rules += [Rule(lhs, RightArrow(), rhs)]
        expr = rhs
    return list(reversed(rules))


def exec(exprs: list[Pattern], rules: list[Rule]):
    expr = exprs[0]
    global VERBOSE
    if VERBOSE:
        print(expr)

    for rule in rules:
        if rule.is_applicable(expr):
            rewritten_expr = rule.apply(expr)
            return exec([rewritten_expr] + exprs[1:], rules)

    is_rule = SINGULAR_RIGHT_ARROW.matches_in(expr)
    if is_rule:
        rules += parse_rules(expr)

    if len(exprs) == 1:
        return expr

    return exec(exprs[1:], rules)


def parse(
    tokens: list[Token],
) -> list[Pattern]:
    exprs = [
        Pattern(*x)
        for x in splitter(lambda t: isinstance(t, End), tokens)
        if len(x) > 0
    ]
    return exprs


RIGHT_ARROW = Pattern.lex(f"_{args.varchar}{args.rightarrow}{args.rightarrow[-1]}?")


class GothicCLI:
    class ExecutionTarget:
        HEADER = "header"
        PIPE = "pipe"
        NONE = None

    def __init__(self):
        self.remaining_rewrites = {}
        self.has_header = False
        self.has_file = False
        self.has_pipe = False
        self.execution_target = None
        result = None

        if args.file is not None:
            with open(args.file, "r") as file:
                file_src = re.sub(r"^#![^\n]+\n", "", file.read())
        else:
            file_src = ""
        self.has_file = args.file is not None

        header_tokens = lex(" ".join(args.exprs) + " " + file_src)
        self.has_header = len(header_tokens) > 0

        # Check if input is being piped in from any source
        pipe_tokens = lex(
            f" {END} ".join(sys.stdin.readlines())
            if not os.isatty(sys.stdin.fileno())
            else ""
        )
        self.has_pipe = len(pipe_tokens) > 0

        if self.has_header:
            self.execution_target = GothicCLI.ExecutionTarget.HEADER
            header_exprs = parse(header_tokens)
            for expr in header_exprs:
                result = self.exec([expr])
                self.reset_rewrite_limits()

        if self.has_pipe:
            self.execution_target = GothicCLI.ExecutionTarget.PIPE
            pipe_exprs = parse(pipe_tokens)
            for expr in pipe_exprs:
                result = self.exec([expr])
                self.reset_rewrite_limits()

        self.execution_target = GothicCLI.ExecutionTarget.NONE

    @property
    def rules(self):
        return self.remaining_rewrites.keys()

    def reset_rewrite_limits(self):
        for rule in self.rules:
            self.remaining_rewrites[rule] = rule.max_rewrites_per_line

    def add_rule(self, rule: Rule):
        self.remaining_rewrites[rule] = rule.max_rewrites_per_line

    def parse_rules(self, expr: Pattern) -> list[Rule]:
        global INTERP_STDIN_RULES
        if (
            self.execution_target == GothicCLI.ExecutionTarget.PIPE
            and not INTERP_STDIN_RULES
        ):
            return []
        rules = []
        rolling_lhs = Pattern()
        while True:
            is_rule, lhs_part, rhs = RIGHT_ARROW.find_match_in(
                expr, keep_remainder=True
            )
            if not is_rule:
                break
            rightarrow_pattern = is_rule[RIGHT_ARROW[0]][
                0
            ]  # uses the token from the RIGHT_ARROW pattern as key into MatchMap and grabs the first (and only) matched rightarrow token
            rightarrow_token = rightarrow_pattern[0]
            rolling_lhs += lhs_part
            rules += [Rule(rolling_lhs, rightarrow_token, rhs)]
            rolling_lhs += rightarrow_pattern
            expr = rhs
        return list(reversed(rules))

    def exec(self, exprs: list[Pattern]):
        expr = exprs[0]

        global VERBOSE
        if VERBOSE:
            print(expr)

        for rule in self.rules:
            if self.remaining_rewrites[rule] > 0 and rule.is_applicable(expr):
                rewritten_expr = rule.apply(expr)
                self.remaining_rewrites[rule] -= 1
                return self.exec([rewritten_expr] + exprs[1:])

        is_rule = any(isinstance(t, RightArrow) for t in expr)
        if is_rule:
            for rule in self.parse_rules(expr):
                self.add_rule(rule)

        if len(exprs) == 1:
            if VERBOSE:
                pass  # already logged
            elif self.has_header and self.has_pipe:
                if self.execution_target == GothicCLI.ExecutionTarget.PIPE:
                    print(expr)
            else:
                print(expr)
            return expr

        return self.exec(exprs[1:])


def goth(src: str):
    """Python function for gothic exec-- not used by CLI."""
    tokens = lex(src)
    exprs = parse(tokens)
    return exec(exprs, rules=[])


def CLI():
    GothicCLI()


if __name__ == "__main__":
    CLI()
