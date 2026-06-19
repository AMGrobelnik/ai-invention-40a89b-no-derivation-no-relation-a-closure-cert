% Closure-certified spatial deduction (RCC-8) -- Mode-B collapse: two paths give disjoint constraints (NTPP vs DC) -> inconsistent reads flagged.
% Per path: compose the stated LOCAL RCC-8 reads (exact GQR table). Then INTERSECT
% the per-path constraints (cross-path closure). Singleton => ANSWER; empty =>
% Mode-B collapse (inconsistent reads flagged, NOT hallucinated); else ABSTAIN.
:- discontiguous pathcomp/2.

% path0: read(A->B)=[ntpp] ; read(B->C)=[ntpp]
pathcomp(p0, [ntpp]).
% path1: read(A->D)=[dc] ; read(D->C)=[ntppi]
pathcomp(p1, [dc]).

inter(R) :- findall(S, pathcomp(_, S), Ss), Ss = [H|T], foldl(isect, T, H, R).
isect(A, B, C) :- findall(X, (member(X, A), member(X, B)), C).
% engine intersection of all path constraints = []
main :- ( inter(R) ->
    ( R = [Single] -> format('QUERY-REL: ~w~nVERDICT: ANSWER(~w)~n', [R, Single])
    ; R = [] -> format('QUERY-REL: []~nVERDICT: COLLAPSE(Mode-B inconsistent)~n', [])
    ; format('QUERY-REL: ~w~nVERDICT: ABSTAIN(non-singleton)~n', [R]) )
  ; write('VERDICT: ABSTAIN(no-path)'), nl ), halt.

:- initialization(main).
