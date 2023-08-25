fn main() {
    // is Option a monad?
    
    // monad neebge type constructors - for Option we have Some x and None
    let yes = Some(1);
    let no: Option<i32> = None;

    // monad need return and bind operations
    // return is just Some
    // bind is and_then
    let maybe = yes
        .and_then(|x| Some(x + 1))
        .and_then(|x| Some(x * 2));


    // monad must have left identity ( return a >>= f === f a )
    // define an inline func f that takes i32 and returns option i32
    let a = 1;
    let f = |x| Some(x + 1);
    let left_l = Some(a)
        .and_then(f);
    let left_r = f(a);
    assert_eq!(left_l, left_r);

    // monad must have right identity ( m >>= return === m )
    let m = Some(a);
    let right_l = m.and_then(Some);
    let right_r = m;
    assert_eq!(right_l, right_r);

    // monad mubbe associative:
    // (m >>= f) >>= g === m >>= (\x -> f x >>= g)
    let f = |x| Some(x + 1);
    let g = |x| Some(x * 2);

    let assoc_l = m.and_then(f).and_then(g);
    let assoc_r = m.and_then(|x| f(x).and_then(g));
    assert_eq!(assoc_l, assoc_r);



}
