% Closure-certified spatial deduction (RCC-8) -- real SpaRP-PS1 closure-certified deduction (SpaRP-PS1_test_1036: 1x0->2).
% Per path: compose the stated LOCAL RCC-8 reads (exact GQR table). Then INTERSECT
% the per-path constraints (cross-path closure). Singleton => ANSWER; empty =>
% Mode-B collapse (inconsistent reads flagged, NOT hallucinated); else ABSTAIN.
:- discontiguous pathcomp/2.

% path0: read(1x0->1)=[tpp] ; read(1->2)=[ntpp]
pathcomp(p0, [ntpp]).

inter(R) :- findall(S, pathcomp(_, S), Ss), Ss = [H|T], foldl(isect, T, H, R).
isect(A, B, C) :- findall(X, (member(X, A), member(X, B)), C).
% engine intersection of all path constraints = [ntpp]
main :- ( inter(R) ->
    ( R = [Single] -> format('QUERY-REL: ~w~nVERDICT: ANSWER(~w)~n', [R, Single])
    ; R = [] -> format('QUERY-REL: []~nVERDICT: COLLAPSE(Mode-B inconsistent)~n', [])
    ; format('QUERY-REL: ~w~nVERDICT: ABSTAIN(non-singleton)~n', [R]) )
  ; write('VERDICT: ABSTAIN(no-path)'), nl ), halt.

:- initialization(main).
