exception NotEqual of string
let check_equal f x y =
    let base = "Values " ^ f x ^ " and " ^ f y ^ " " in ();
    if x <> y then
        raise (NotEqual (base ^ "are not equal"))
    else
        print_newline (print_string (base ^ "are equal"))
;;

(* 1 *)
let rec last_mine = function
    | [] -> None
    | h :: [] -> Some h
    | _ :: t -> last_mine t

let rec last_ex = function
    | [] -> None
    | [ x ] -> Some x
    | _ :: t -> last_ex t


    (* 2 *)
(* got same soln as example *)
let rec last_two_mine = function
    | [] | [ _ ]-> None
    | [ h; t ] -> Some (h, t)
    | _ :: t -> last_two_mine t


    (* 3 *)
let rec _nth l c n =
    match l, c, n with
    | [], _, _ -> None
    | h :: _, c, n when c = n -> Some h
    | _ :: t, c, n -> _nth t (c + 1) n

let nth l n = _nth l 0 n


let rec at k = function
    | [] -> None
    | h :: t -> if k = 0 then Some h else at (k - 1) t

    (* 4 *)
let length list =
    let rec aux n = function
        | [] -> n
        | _ :: t -> aux (n + 1) t
    in
    aux 0 list;;

(* 5 *)
let rec rev = function
    | [] -> []
    | h :: t -> (rev t) @ [ h ]

let rev2 list =
    let rec aux acc = function
        | [] -> acc
        | h :: t -> aux (h :: acc) t  (* basically just popping off one list pushing onto front of another *)
    in
    aux [] list

(* 6 *)
let is_palindrome list =
    list = rev list

let cancer_palindrome l =
    let l_rev = rev l in
        let rec palindrome_aux one two = match one, two with
            | [], [] -> true
            | h :: t, hr :: tr -> if h != hr then false else palindrome_aux t tr
            | _, _ -> false
        in
        palindrome_aux l l_rev

(* 7 *)
type 'a node =
    | One of 'a
    | Many of 'a node list

(* takes in input list l, defines recursive aux fn that takes an extra param for the flattened list *)
(* calls aux [] l *)
(* if l is empty, returns empty, if l's head is One, appends it to flat and concatenates that with aux flat t *)
(* if l's head is many, concats aux flat h with aux flat t *)
let flatten l =
    let rec aux flat = function
    | [] -> []
    | One h :: t -> h :: flat @ aux flat t
    | Many h :: t -> aux flat h @ aux flat t
    in aux [] l

(* this was the example solution. I'm guessing maybe mine is way less efficient? *)
let flatten_ex list =
    let rec aux acc = function
        | [] -> acc
        | One x :: t -> aux (x :: acc) t
        | Many l :: t -> aux (aux acc l) t
    in
        List.rev (aux [] list)

(* 8 *)
let compress list =
    let rec aux last out = function
        | [] -> out
        | h :: t ->
            if Option.is_some last && Option.get last = h
            then aux (Some h) out t
            else aux (Some h) (h :: out) t
    in List.rev (aux None [] list)

(* their example is muchhh more elegante *)
let rec compress_ex = function
    | a :: (b :: _ as t) -> if a = b then compress_ex t else a :: compress_ex t
    | smaller -> smaller

let () =
    (* 1 *)
    let mine = Option.is_some (last_mine []) in ();
    let ex = Option.is_some (last_ex []) in ();
    check_equal string_of_bool mine ex;
    let mine = Option.get (last_mine [ 1; 2; 3; ]) in ();
    let ex = Option.get (last_ex [ 1; 2; 3;]) in ();
    check_equal string_of_int mine ex;

    (* 2 *)
    let _ = last_two_mine [ 1; 2; 3; 4; ] in ();
    let _ = last_two_mine [] in ();

    (* 3 *)
    check_equal string_of_int (Option.get (nth [ 0; 1; 2; 3; 4; ] 2)) 2;
    check_equal string_of_int (Option.get (nth [ 3; 4; 5;] 1)) 4;
    check_equal string_of_int (Option.get (nth [0; 1; 2; 3; 4;] 2)) (Option.get (at 2 [0; 1; 2; 3; 4;]));

    (* 4 *)
    let _ = length [1; 2; 3;] in ();

    (* 5 *)
    check_equal string_of_bool (rev [1; 2; 3;] = [3; 2; 1;]) true;
    check_equal string_of_bool (rev [1; 3; 7; 2;] = rev2 [1; 3; 7; 2;]) true;

    check_equal string_of_bool (is_palindrome [ 1; 2; 3; 2; 1;]) true;
    check_equal string_of_bool (cancer_palindrome [ 1; 2; 3; 2; 1;]) true;
    check_equal string_of_bool (cancer_palindrome [ 1; 2; 3; 4; 5]) false;
    check_equal string_of_bool (flatten [One "a"; Many [One "b"; Many [One "c" ;One "d"]; One "e"]] = [ "a" ; "b" ; "c" ; "d" ; "e" ]) true;

    let _ =
        flatten [One "a"; Many [One "b"; Many [One "c" ;One "d"]; One "e"]]
        |> List.iter print_endline
    in ();

    let mine = flatten [One "a"; Many [One "b"; Many [One "c" ;One "d"]; One "e"]] in
        let ex = flatten_ex [One "a"; Many [One "b"; Many [One "c" ;One "d"]; One "e"]]
            in check_equal string_of_bool (mine = ex) true;

    let _ =
        compress ["a"; "a"; "a"; "a"; "b"; "c"; "c"; "a"; "a"; "d"; "e"; "e"; "e"; "e"]
        |> List.iter print_endline in ();

    let mine = compress ["a"; "a"; "a"; "a"; "b"; "c"; "c"; "a"; "a"; "d"; "e"; "e"; "e"; "e"] in
    let ex = compress_ex ["a"; "a"; "a"; "a"; "b"; "c"; "c"; "a"; "a"; "d"; "e"; "e"; "e"; "e"]  in
        check_equal string_of_bool (mine = ex) true;


;;
