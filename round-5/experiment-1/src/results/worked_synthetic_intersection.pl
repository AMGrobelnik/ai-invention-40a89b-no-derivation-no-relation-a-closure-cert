% Closure-certified spatial deduction (RCC-8) -- synthetic cross-path intersection: best-single ['DC', 'NTPPi', 'TPPi'] (non-singleton) narrowed by intersecting two paths (p1=['DC', 'EC', 'NTPP', 'PO', 'TPP'], p2=['DC', 'NTPPi', 'TPPi']) to ['DC'].
% Per path: compose the stated LOCAL RCC-8 reads (exact GQR table). Then INTERSECT
% the per-path constraints (cross-path closure). Singleton => ANSWER; empty =>
% Mode-B collapse (inconsistent reads flagged, NOT hallucinated); else ABSTAIN.
:- discontiguous pathcomp/2.

% path0: read(S->W1)=[dc] ; read(W1->T)=[ec]
pathcomp(p0, [dc,ec,ntpp,po,tpp]).
% path1: read(S->W2)=[dc,tppi] ; read(W2->T)=[tppi]
pathcomp(p1, [dc,ntppi,tppi]).

inter(R) :- findall(S, pathcomp(_, S), Ss), Ss = [H|T], foldl(isect, T, H, R).
isect(A, B, C) :- findall(X, (member(X, A), member(X, B)), C).
% engine intersection of all path constraints = [dc]
main :- ( inter(R) ->
    ( R = [Single] -> format('QUERY-REL: ~w~nVERDICT: ANSWER(~w)~n', [R, Single])
    ; R = [] -> format('QUERY-REL: []~nVERDICT: COLLAPSE(Mode-B inconsistent)~n', [])
    ; format('QUERY-REL: ~w~nVERDICT: ABSTAIN(non-singleton)~n', [R]) )
  ; write('VERDICT: ABSTAIN(no-path)'), nl ), halt.

:- initialization(main).
