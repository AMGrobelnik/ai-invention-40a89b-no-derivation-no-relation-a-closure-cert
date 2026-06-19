% Closure-certified temporal deduction (Allen-13) -- auto-generated trace program.
% Query: relation of e_ABC19980108_1830_0711__e28 to e_ABC19980108_1830_0711__e67 (held out), recovered by intersecting
% the compositions of >=2 edge-disjoint LOCAL-read paths (path-consistency narrowing).
:- discontiguous pathcomp/2.

% --- per disjoint-path composition of the two LOCAL Allen reads (engine-computed) ---
% via e_ABC19980108_1830_0711__e11: read(S,e_ABC19980108_1830_0711__e11)=[bi] o read(e_ABC19980108_1830_0711__e11,T)=[b,bi,d,di,e,f,fi,m,mi,o,oi,s,si]
pathcomp(e_ABC19980108_1830_0711__e11, [b,bi,d,di,e,f,fi,m,mi,o,oi,s,si]).
% via e_ABC19980108_1830_0711__e12: read(S,e_ABC19980108_1830_0711__e12)=[bi] o read(e_ABC19980108_1830_0711__e12,T)=[bi,di,e,fi,mi,oi,si]
pathcomp(e_ABC19980108_1830_0711__e12, [bi]).
% via e_ABC19980108_1830_0711__e147: read(S,e_ABC19980108_1830_0711__e147)=[b,bi,d,di,e,f,fi,m,mi,o,oi,s,si] o read(e_ABC19980108_1830_0711__e147,T)=[bi,di,e,fi,mi,oi,si]
pathcomp(e_ABC19980108_1830_0711__e147, [b,bi,d,di,e,f,fi,m,mi,o,oi,s,si]).
% via e_ABC19980108_1830_0711__e16: read(S,e_ABC19980108_1830_0711__e16)=[bi] o read(e_ABC19980108_1830_0711__e16,T)=[b,bi,d,di,e,f,fi,m,mi,o,oi,s,si]
pathcomp(e_ABC19980108_1830_0711__e16, [b,bi,d,di,e,f,fi,m,mi,o,oi,s,si]).
% via e_ABC19980108_1830_0711__e17: read(S,e_ABC19980108_1830_0711__e17)=[bi] o read(e_ABC19980108_1830_0711__e17,T)=[b,bi,d,di,e,f,fi,m,mi,o,oi,s,si]
pathcomp(e_ABC19980108_1830_0711__e17, [b,bi,d,di,e,f,fi,m,mi,o,oi,s,si]).
% via e_ABC19980108_1830_0711__e18: read(S,e_ABC19980108_1830_0711__e18)=[bi] o read(e_ABC19980108_1830_0711__e18,T)=[b,bi,d,di,e,f,fi,m,mi,o,oi,s,si]
pathcomp(e_ABC19980108_1830_0711__e18, [b,bi,d,di,e,f,fi,m,mi,o,oi,s,si]).
% via e_ABC19980108_1830_0711__e19: read(S,e_ABC19980108_1830_0711__e19)=[bi,di,e,fi,mi,oi,si] o read(e_ABC19980108_1830_0711__e19,T)=[b,bi,d,di,e,f,fi,m,mi,o,oi,s,si]
pathcomp(e_ABC19980108_1830_0711__e19, [b,bi,d,di,e,f,fi,m,mi,o,oi,s,si]).
% via e_ABC19980108_1830_0711__e20: read(S,e_ABC19980108_1830_0711__e20)=[b,bi,d,di,e,f,fi,m,mi,o,oi,s,si] o read(e_ABC19980108_1830_0711__e20,T)=[b,bi,d,di,e,f,fi,m,mi,o,oi,s,si]
pathcomp(e_ABC19980108_1830_0711__e20, [b,bi,d,di,e,f,fi,m,mi,o,oi,s,si]).
% via e_ABC19980108_1830_0711__e21: read(S,e_ABC19980108_1830_0711__e21)=[bi,di,e,fi,mi,oi,si] o read(e_ABC19980108_1830_0711__e21,T)=[b,bi,d,di,e,f,fi,m,mi,o,oi,s,si]
pathcomp(e_ABC19980108_1830_0711__e21, [b,bi,d,di,e,f,fi,m,mi,o,oi,s,si]).
% via e_ABC19980108_1830_0711__e3: read(S,e_ABC19980108_1830_0711__e3)=[b,bi,d,di,e,f,fi,m,mi,o,oi,s,si] o read(e_ABC19980108_1830_0711__e3,T)=[b,d,e,f,m,o,s]
pathcomp(e_ABC19980108_1830_0711__e3, [b,bi,d,di,e,f,fi,m,mi,o,oi,s,si]).

% intersection of all path compositions = the certified query relation set
inter(R) :- findall(S, pathcomp(_, S), Ss), Ss = [H|T], foldl(intersect, T, H, R).
intersect(A, B, C) :- findall(X, (member(X, A), member(X, B)), C).
main :- ( inter(R) ->
    ( R = [Single] -> format('INTERSECTION: ~w~nVERDICT: ANSWER(~w)~n', [R, Single])
    ; R = [] -> format('INTERSECTION: []~nVERDICT: COLLAPSE(Mode-B inconsistent)~n', [])
    ; format('INTERSECTION: ~w~nVERDICT: ABSTAIN(non-singleton)~n', [R]) )
  ; write('VERDICT: ABSTAIN(no-paths)'), nl ),
  halt.

:- initialization(main).
