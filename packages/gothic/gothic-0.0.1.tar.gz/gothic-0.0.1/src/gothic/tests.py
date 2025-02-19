#!/usr/bin/python
from .main import lex, MatchMap, Pattern, Rule, goth, parse_rules, RightArrow


def test_goth_0():
    result = goth(
        """
        map f' . .. ] => f' . map f' .. ] ;
        map f' .    ] => f' .             ;

        map +1 1 2 3 ]                    ;
        """
    )
    assert result == Pattern(*lex("+1 1 +1 2 +1 3"))


def test_goth_1():
    result = goth(
        """
        x => x'kek ;
        x => bruh  ;
        kek        ;
        """
    )
    assert result == Pattern(*lex("bruh"))


def test_goth_2():
    result = goth(
        """
        x'x' => x'kek ;
        x' => bruh    ;
        shrek         ;
        """
    )
    assert result == Pattern(*lex("shrek"))


def test_goth_3():
    result = goth(
        """
        # .. # => ;

        # 
         this is fuckin arithmetic bitch, but only for the natural nums
         NO NEGATIVE NANCY'S ALLOWED!
        # ;

        x => x''/ ;
        y => y''/ ;

        x + y => x y ;
        x + 0 => x   ;
        0 + y =>   y ;
        0 + 0 =>     ;

        x - x =>   ;
        x - 0 => x ;

        / + 0 + / / / / / - 0 - / / / + 0 + 0 - 0 ;
        """
    )
    assert result == Pattern(*lex("/ / /"))


def test_goth_4():
    result = goth(
        r"""
        map f' . rest'' ] => f' . map f' rest'' ] ;
        map f' . ] => f' . ;
        1337 a => 4 ;
        1337 b => |3 ;
        1337 c => < ;
        1337 d => |] ;
        1337 e => 3 ;
        1337 f => |= ;
        1337 g => 6 ;
        1337 h => |n ;
        1337 i => : ;
        1337 j => _| ;
        1337 k => |< ;
        1337 l => |_ ;
        1337 m => /\/\ ;
        1337 n => /\/ ;
        1337 o => 0 ;
        1337 p => |^ ;
        1337 q => ? ;
        1337 r => /- ;
        1337 s => $ ;
        1337 t => + ;
        1337 u => |_| ;
        1337 v => \/ ;
        1337 w => \/\/ ;
        1337 x => >< ;
        1337 y => ^/ ;
        1337 z => % ;
        1337 _ => _ ;
        map 1337 e r a n d a l e x ] ;
        """
    )
    assert result == Pattern(*lex(r"3 /- 4 /\/ |] 4 |_ 3 ><"))


def test_goth_5():
    base_rules = """
        [ T and T ] => T ;
        [ T and F ] => F ;
        [ F and T ] => F ;
        [ F and F ] => F ;

        [ T or T ] => T ;
        [ T or F ] => T ;
        [ F or T ] => T ;
        [ F or F ] => F ;

        not T => F ;
        not F => T ;

        if T then .. else .. fi => .. ;
        if F then .. else .. fi => disregard [ .. ] .. ;

        disregard [ .. ] => ;

        x' = x' => T ;
        x' = y' => F ;
    """

    result = goth(
        f"""
        {base_rules}

        if 1 = 2 then A else B fi ;
        """
    )
    assert result == Pattern(*lex("B"))

    result = goth(
        f"""
        {base_rules}

        Hitler = Cool ;
        """
    )
    assert result == Pattern(*lex("F"))

    result = goth(
        f"""
        {base_rules}

        Hitler = Hitler ;
        """
    )
    assert result == Pattern(*lex("T"))

    result = goth(
        f"""
        {base_rules}

        A => [ p or q ] ;
        B => [ q and r ] ;
        p => T ;
        q => F ;
        r => T ;
        if not [ A and B ] then p else r fi ;
        """
    )
    assert result == Pattern(*lex("T"))


def test_goth_6():
    result = goth(
        """
        # .. # => ;

        x => x''/ ;
        y => y''/ ;

        x + y => x y ;
        x + 0 => x ;
        0 + y => y ;
        0 + 0 => 0 ;

        x y - x => y ;
        x - x => 0 ;
        x - 0 => x ;
        0 - 0 => 0 ;

        fib / n''/ => fib n''/ + fib n''/ - / ;
        fib / => / ;
        fib 0 => 0 ;

        # fib results expected
        0 1 2  3 	 4   5
        0 / /  //  /// /////
        # ;

        # def of equal sequences # ;
        x'' = x'' => T ;
        x'' = y'' => F ;

        # checking that fib(6) = 8 # ;
        / / / / / / / / = fib / / / / / / ;
        """
    )
    assert result == Pattern(*lex("T"))


def test_goth_7():
    result = goth(
        """
        # .. # => ;

        one => . ;
        some => .. ;

        map f' one some ] => f' one map f' some ] ;
        map f' one ] => f' one ;

        map F 1 2 3 ] ;
        """
    )
    assert result == Pattern(*lex("F 1 F 2 F 3"))

    result = goth(
        """
        # .. # => ;
        again .. => .. .. ;

        # note: you might intuitively expect the output to be "a b c a b c",
        but the current implementation of wildcard rewriting only matches in order,
        without looping back around to front of lhs if it is exhausted before rhs.
        So this is behaving as intended, for now-- we can maybe reconsider this in the future # ;
        again a b c ;
        """
    )
    assert result == Pattern(*lex("a b c .."))

    result = goth(
        """
        again_4_real x'' => x'' x'' ;
        # how you can actually do it ---> # ; again_4_real a b c ;
        """
    )
    assert result == Pattern(*lex("a b c a b c"))

    result = goth(
        """
        x => x' ;
        xs => xs'' ;

        x ;
        xs ;
        """
    )
    assert result == Pattern(*lex("xs''"))


def test_goth_8():
    result = goth(
        """
        L => L''^(?!=>).* ;
        x => last'^(?!=>).* ;
        backwards L x => x backwards L ;
        backwards x => x ;

        backwards 1 2 3 ;
        """
    )
    assert result == Pattern(*lex("3 2 1"))


def test_goth_9():
    result = goth(
        """
        # .. # => ;

        # the following tests a version of map that terminates its scan at the first instance of ] # ;

        not] => rest''(?!^]$).* ;
        map f' . ] => f' . ;
        map f' . not] => f' . map f' not] ;

        map ^2 1 2 3 ] map kek a b c ] ;
        """
    )
    assert result == Pattern(*lex("^2 1 ^2 2 ^2 3 kek a kek b kek c"))


def test_goth_10():
    result = goth(
        """
        # .. # => ;

        x x x x x x x x x x => 10 ;
        x x x x x x x x x => 9 ;
        x x x x x x x x => 8 ;
        x x x x x x x => 7 ;
        x x x x x x => 6 ;
        x x x x x => 5 ;
        x x x x => 4 ;
        x x x => 3 ;
        x x => 2 ;
        x => 1 ;

        9 10 => 10 0 ;
        8 10 => 9 ;
        7 10 => 8 ;
        6 10 => 7 ;
        5 10 => 6 ;
        4 10 => 5 ;
        3 10 => 4 ;
        2 10 => 3 ;
        1 10 => 2 ;
        0 10 => 1 ;
        10 => 1 ;

        # 127 # ;
        x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x ;
        """
    )
    assert result == Pattern(*lex("1 2 7"))


def test_goth_11():
    result = goth(
        """
        10 => 1 1 1 1 1 1 1 1 1 1 ;
        9 => 1 1 1 1 1 1 1 1 1 ;
        8 => 1 1 1 1 1 1 1 1 ;
        7 => 1 1 1 1 1 1 1 ;
        6 => 1 1 1 1 1 1 ;
        5 => 1 1 1 1 1 ;
        4 => 1 1 1 1 ;
        3 => 1 1 1 ;
        2 => 1 1 ;

        1 1 + 1 1 => 1 1 1 + 1 ;
        1 1 + 1 => 1 1 1 ;
        1 + 1 1 => 1 1 1 ;
        1 + 1 => 1 1 ;

        1 1 - 1 1 => 1 - 1 ;
        1 1 - 1 => 1 ;
        1 - 1 => ;

        1 1 > 1 1 => 1 > 1 ;
        1 > 1 1 => F ;
        1 1 > 1 => T ;
        1 > 1 => F ;

        1 1 < 1 1 => 1 < 1 ;
        1 < 1 1 => T ;
        1 1 < 1 => F ;
        1 < 1 => F ;

        [ .. . = . .. ] => . = . and [ .. = .. ] ;
        [ .. . = . ] => F ;
        [ . = . .. ] => F ;
        [ . = . ] => . = . ;
        x' = x' => T ;
        x' = y' => F ;

        T and T => T ;
        T and F => F ;
        F and T => F ;
        F and F => F ;

        if T then .. else .. fi => .. ;
        if F then .. else .. fi => delete [ .. ] .. ;
        delete [ .. ] => ;

        if [ 1 + 1 = 2 ] and 7 - 4 > 1 + 1 then Math is working. else Math is broken! fi ;
        """
    )
    assert result == Pattern(*lex("Math is working."))


def test_polymorphic_rule_parse():
    expr = Pattern(*lex("a => b => x => y"))
    rules = parse_rules(expr)

    lhs2 = Pattern(*lex("a"))
    rhs2 = Pattern(*lex("b => x => y"))
    assert rules[2].lhs == lhs2
    assert rules[2].rhs == rhs2

    lhs1 = Pattern(*lex("a => b"))
    rhs1 = Pattern(*lex("x => y"))
    assert rules[1].lhs == lhs1
    assert rules[1].rhs == rhs1

    lhs0 = Pattern(*lex("a => b => x"))
    rhs0 = Pattern(*lex("y"))
    assert rules[0].lhs == lhs0
    assert rules[0].rhs == rhs0


def test_goth_polymorphic_rule0():
    result = goth(
        """
        flip_sides 
            lhs'' => rhs'' 
                =>
            rhs'' => lhs'' 
        ;
        flip_sides x => y ;
        """
    )
    assert result == Pattern(*lex("y => x"))


def test_goth_polymorphic_rule1():
    result = goth(
        """
        flip_sides 
            lhs'' => rhs'' 
                =>
            rhs'' => lhs'' 
        ;
        flip_sides a => b => x => y ;
        """
    )
    assert result == Pattern(*lex("y => a => b => x"))


def test_rule_0():
    lhs = Pattern(*lex("map f' . .."))
    rhs = Pattern(*lex("f' . map .."))
    rule = Rule(lhs, RightArrow(), rhs)
    x = Pattern(*lex("please ignore me I am innocent map +1 1 2 3 wheeeeeeeee x y z"))
    rewritten_x = rule.apply(x)
    expected_pattern = Pattern(
        *lex("please ignore me I am innocent +1 1 map 2 3 wheeeeeeeee x y z")
    )
    # print("lhs:", lhs)
    # print("rhs:", rhs)
    # print("x:", x)
    # print("rewritten_x:", rewritten_x)
    assert rewritten_x == expected_pattern

    lhs = Pattern(*lex("$ .. kek x' .. ;; ;"))
    rhs = Pattern(*lex("kek .. .. x'"))
    rule = Rule(lhs, RightArrow(), rhs)
    x = Pattern(
        *lex(
            "a b $ c d kek e f u c k ;; ; hello I am on the right side I am a good boy"
        )
    )
    rewritten_x = rule.apply(x)
    expected_pattern = Pattern(
        *lex("a b kek c d f u c k e hello I am on the right side I am a good boy")
    )
    # print("lhs:", lhs)
    # print("rhs:", rhs)
    # print("x:", x)
    # print("rewritten_x:", rewritten_x)
    assert rewritten_x == expected_pattern

    # left annihilation
    lhs = Pattern(*lex("X"))
    rhs = Pattern()
    rule = Rule(lhs, RightArrow(), rhs)
    x = Pattern(*lex("X <-die"))
    rewritten_x = rule.apply(x)
    expected_pattern = Pattern(*lex("<-die"))
    # print("lhs:", lhs)
    # print("rhs:", rhs)
    # print("x:", x)
    # print("rewritten_x:", rewritten_x)
    assert rewritten_x == expected_pattern

    # middle annihilation
    lhs = Pattern(*lex("X"))
    rhs = Pattern()
    rule = Rule(lhs, RightArrow(), rhs)
    x = Pattern(*lex("perish-> X <-die"))
    rewritten_x = rule.apply(x)
    expected_pattern = Pattern(*lex("perish-> <-die"))
    # print("lhs:", lhs)
    # print("rhs:", rhs)
    # print("x:", x)
    # print("rewritten_x:", rewritten_x)
    assert rewritten_x == expected_pattern

    # right annihilation
    lhs = Pattern(*lex("X"))
    rhs = Pattern()
    rule = Rule(lhs, RightArrow(), rhs)
    x = Pattern(*lex("perish-> X"))
    rewritten_x = rule.apply(x)
    expected_pattern = Pattern(*lex("perish->"))
    # print("lhs:", lhs)
    # print("rhs:", rhs)
    # print("x:", x)
    # print("rewritten_x:", rewritten_x)
    assert rewritten_x == expected_pattern

    # total annihilation
    lhs = Pattern(*lex("X"))
    rhs = Pattern()
    rule = Rule(lhs, RightArrow(), rhs)
    x = Pattern(*lex("X"))
    rewritten_x = rule.apply(x)
    expected_pattern = Pattern()
    # print("lhs:", lhs)
    # print("rhs:", rhs)
    # print("x:", x)
    # print("rewritten_x:", rewritten_x)
    assert rewritten_x == expected_pattern


def test_rewrite_0():
    lhs = Pattern(*lex("map f' . .."))
    rhs = Pattern(*lex("f' . map .."))
    x = Pattern(*lex("map +1 1 2 3"))
    # #print(lhs)
    # #print(rhs)
    # #print(x)
    match_map = lhs.find_match_in(x)
    rewritten_pattern = match_map.rewrite(rhs)
    # #print("rewritten_pattern", rewritten_pattern)
    # #print("type:", type(rewritten_pattern))
    expected_pattern = Pattern(*lex("+1 1 map 2 3"))
    # #print("expected_pattern", expected_pattern)
    # #print("type:", type(expected_pattern))
    assert rewritten_pattern == expected_pattern

    lhs = Pattern(*lex("map f' x' xs''"))
    rhs = Pattern(*lex("f' x' map xs''"))
    x = Pattern(*lex("map +1 1 2 3"))
    # #print(lhs)
    # #print(rhs)
    # #print(x)
    match_map = lhs.find_match_in(x)
    # #print(match_map)
    rewritten_pattern = match_map.rewrite(rhs)
    # #print("rewritten_pattern", rewritten_pattern)
    # #print("type:", type(rewritten_pattern))
    # #print(rewritten_pattern)
    expected_pattern = Pattern(*lex("+1 1 map 2 3"))
    # #print("expected_pattern", expected_pattern)
    # #print("type:", type(expected_pattern))
    assert rewritten_pattern == expected_pattern

    lhs = Pattern(*lex(".. kek x' .."))
    rhs = Pattern(*lex("kek .. .. x'"))
    x = Pattern(*lex("a b c d kek e f u c k"))
    # #print(lhs)
    # #print(rhs)
    # #print(x)
    match_map = lhs.find_match_in(x)
    # #print(match_map)
    rewritten_pattern = match_map.rewrite(rhs)
    # #print("rewritten_pattern", rewritten_pattern)
    # #print("type:", type(rewritten_pattern))
    expected_pattern = Pattern(*lex("kek a b c d f u c k e"))
    # #print("expected_pattern", expected_pattern)
    # #print("type:", type(expected_pattern))
    assert rewritten_pattern == expected_pattern

    lhs = Pattern(*lex(".. kek x' .. ubervar'' => randomshit ;"))
    rhs = Pattern(*lex("kek .. .. x'"))
    x = Pattern(
        *lex("a b c d kek e f u c k ooga booga mooka tooka rooka sooka => randomshit ;")
    )
    # #print(lhs)
    # #print(rhs)
    # #print(x)
    match_map = lhs.find_match_in(x)
    # #print(match_map)
    rewritten_pattern = match_map.rewrite(rhs)
    # #print("rewritten_pattern", rewritten_pattern)
    # #print("type:", type(rewritten_pattern))
    expected_pattern = Pattern(
        *lex("kek a b c d f u c k ooga booga mooka tooka rooka e")
    )
    # #print("expected_pattern", expected_pattern)
    # #print("type:", type(expected_pattern))
    assert rewritten_pattern == expected_pattern


def test0():
    print(lex(input()))


def test1():
    a = Pattern(*lex("hello there buddy"))
    b = Pattern(*lex("hello there buddy"))
    # print(a)
    # print(b)
    # print(a.matches_beginning(b))
    assert a.matches_beginning(b)


def test2():
    a = Pattern(*lex("x' => x'"))
    b = Pattern(*lex("1 => 1"))
    # print(a)
    # print(b)
    # print(a.matches_beginning(b))
    assert a.matches_beginning(b)

    a = Pattern(*lex("x' = x'"))
    b = Pattern(*lex("1 = 2"))
    # print(a)
    # print(b)
    # print(a.matches_beginning(b))
    assert not a.matches_beginning(b)

    a = Pattern(*lex("x'' = x'"))
    b = Pattern(*lex("1 = 2"))
    # print(a)
    # print(b)
    # print(a.matches_beginning(b))
    assert a.matches_beginning(b)


def test3():
    a = Pattern(*lex("x'' = x''"))
    b = Pattern(*lex("1 1 = 1 1"))
    # print(a)
    # print(b)
    # print(a.matches_beginning(b))
    assert a.matches_beginning(b)

    a = Pattern(*lex("x'' = x''"))
    b = Pattern(*lex("1 = 2"))
    # print(a)
    # print(b)
    # print(a.matches_beginning(b))
    assert not a.matches_beginning(b)


def test4():
    a = Pattern(*lex("map f' . .."))
    b = Pattern(*lex("map f x"))
    # print(a)
    # print(b)
    # print(a.matches_beginning(b))
    assert not a.matches_beginning(b)

    a = Pattern(*lex("map f' . .."))
    b = Pattern(*lex("map f x y"))
    # print(a)
    # print(b)
    # print(a.matches_beginning(b))
    assert a.matches_beginning(b)

    a = Pattern(*lex("map f' h' xs''"))
    b = Pattern(*lex("map f x"))
    # print(a)
    # print(b)
    # print(a.matches_beginning(b))
    assert not a.matches_beginning(b)

    a = Pattern(*lex("map f' h' xs''"))
    b = Pattern(*lex("map f x y z"))
    # print(a)
    # print(b)
    # print(a.matches_beginning(b))
    assert a.matches_beginning(b)

    a = Pattern(*lex("map f' h' xs'' h' xs''"))
    b = Pattern(*lex("map f x y z x y z"))
    # print(a)
    # print(b)
    # print(a.matches_beginning(b))
    assert a.matches_beginning(b)

    a = Pattern(*lex("map f' h' xs'' h' xs''"))
    b = Pattern(*lex("map f x za za y z x y z"))
    # print(a)
    # print(b)
    # print(a.matches_beginning(b))
    assert not a.matches_beginning(b)


def test5():
    a = Pattern(*lex("yo .. yo"))
    b = Pattern(*lex("hi hello yo some random bs yo"))
    # print(a)
    # print(b)
    # print(a.matches_in(b))
    assert a.matches_in(b)

    a = Pattern(*lex("yo .. yo"))
    b = Pattern(*lex("hi hello yo some yo random bs yo"))
    # print(a)
    # print(b)
    # print(a.matches_in(b))
    assert a.matches_in(b)


def test_match_obj_generation():
    a = Pattern(*lex("map f' . .."))
    b = Pattern(*lex("map +1 1 2 3"))
    # #print(a)
    # #print(b)
    # #print(a.matches_beginning(b))
    assert a.matches_beginning(b) is not None

    a = Pattern(*lex("x'1|2 + x'1|2 = y'"))
    b = Pattern(*lex("1 + 1 = 3"))
    # #print(a)
    # #print(b)
    # #print(a.matches_beginning(b))
    assert a.matches_beginning(b) is not None

    a = Pattern(*lex(".. = .."))
    b = Pattern(*lex("1 2 3 = 1 2 3"))
    # #print(a)
    # #print(b)
    # #print(a.matches_beginning(b))
    assert a.matches_beginning(b) is not None

    a = Pattern(*lex(".. = a b c"))
    b = Pattern(*lex("1 2 3 = 1 2 3"))
    # # #print(a)
    # # #print(b)
    # # #print(a.matches_beginning(b))
    assert a.matches_beginning(b) is None

    a = Pattern(*lex("f .. = L'' .. L'' a b c"))
    b = Pattern(*lex("f 1 2 3 = 1 2 3 $ 1 2 k 3 a b c"))
    # # #print(a)
    # # #print(b)
    # #print(a.matches_beginning(b))
    assert a.matches_beginning(b) is None


def test_antimatch():
    result = goth(
        f"""
        x => x'![]] ;
        xs => xs''![]] ;
        map f' x xs ] => f' x map f' xs ] ;
        map f' x ] => f' x ;
        map f 1 2 ] 3 ;
         """
    )
    assert result == Pattern(*lex("f 1 f 2 3"))


def run_tests():
    test_functions = [
        test_goth_0,
        test_goth_1,
        test_goth_2,
        test_goth_3,
        test_goth_4,
        test_goth_5,
        test_goth_6,
        test_goth_7,
        test_goth_8,
        test_goth_9,
        test_goth_10,
        test_goth_11,
        test_rule_0,
        test_rewrite_0,
        test1,
        test2,
        test3,
        test4,
        test5,
        test_match_obj_generation,
        test_polymorphic_rule_parse,
        test_goth_polymorphic_rule0,
        test_goth_polymorphic_rule1,
        test_antimatch,
    ]

    for test_func in test_functions:
        try:
            test_func()
            print(f"{test_func.__name__}: PASS")
        except AssertionError:
            print(f"{test_func.__name__}: FAIL")


if __name__ == "__main__":
    run_tests()
