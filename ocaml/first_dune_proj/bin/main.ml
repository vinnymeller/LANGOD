open Graphics;;
let () = 
    print_endline "Hello, World!";
    open_graph " 640x480";
    set_window_title "My Graphics Window";
    moveto 320 240;
    draw_string "Hello, Graphics";
    ignore (read_line ());
    close_graph ();;


