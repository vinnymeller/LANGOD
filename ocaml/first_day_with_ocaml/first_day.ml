let () =
    print_endline (string_of_int 42);;

let () =
    print_int 42;
    print_newline ();;

let () =
    print_int (let y = 50 in y * y);
    print_newline ();;

let square x = x * x;;

print_int (square 30);
print_newline ();;

let square_is_even x =
    square x mod 2 = 0;;

print_endline (string_of_bool (square_is_even 30));;

let ordered a b c =
    a <= b && b <= c;;

print_endline ("1 2 3 is ordered: " ^ string_of_bool (ordered 1 2 3));;
print_endline ("2 1 3 is ordered: " ^ string_of_bool (ordered 2 1 3));;

let average a b = 
    (a +. b) /. 2.0;;

print_newline (print_float (average 2.0 4.0));
print_newline (print_float (average 3.5 11.71));;

let rec range a b =
    if a > b then []
    else a :: range (a + 1) b;;

print_endline (string_of_int (List.length (range 1 10)));;

let rec print_int_list l = match l with
    | [] -> ()
    | h :: t -> print_newline (print_int h); print_int_list t;;

(* print all the numbers in the list *)
let range_list = range 1 10;;
print_int_list range_list;;

