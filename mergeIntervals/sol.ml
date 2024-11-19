  let shouldMerge (_, a1) (b0, _) = if a1 >= b0 then true else false
  let mergeTwo (a0,a1) (b0, b1) = (min a0 b0, max a1 b1)

  let merge a = 
    let rec aux ls prev acc = match ls with
    | [] -> prev::acc
    | hd :: tl when shouldMerge prev hd -> aux tl (mergeTwo prev hd) acc
    | hd :: tl -> aux tl hd (prev::acc)
    in
    match a with
      | [] -> failwith "nah"
    | hd::tl -> List.rev(aux tl hd [])


  let () =
    let result = merge [(1, 3); (2, 6); (8, 10); (11, 12);(15, 18)] in
    List.iter (fun (a, b) -> Printf.printf "(%d, %d)\n" a b) result;
    print_newline ()


  let () =
    let result = merge [1,4;4,5] in
    List.iter (fun (a, b) -> Printf.printf "(%d, %d)\n" a b) result;
    print_newline ()
