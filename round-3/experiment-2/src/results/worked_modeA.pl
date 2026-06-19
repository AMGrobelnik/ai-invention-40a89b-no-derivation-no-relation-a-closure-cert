% Closure-certified temporal deduction -- auto-generated trace program.
% Convex point start-point algebra over event start points {lt,eq,gt}.
% The query relation is the INTERSECTION of all length-2 path compositions
% (path-consistency narrowing); an empty intersection certifies inconsistency.
:- discontiguous rel/3.

% --- composition table (Vilain-Kautz convex point algebra) ---
comp(lt,lt,lt).
comp(lt,eq,lt).
comp(eq,lt,lt).
comp(eq,eq,eq).
comp(eq,gt,gt).
comp(gt,eq,gt).
comp(gt,gt,gt).

% --- read facts (LOCAL LLM reads; both directions via converse) ---
rel(e_NYT19980206_0466__ei523,e_NYT19980206_0466__ei519,eq).
rel(e_NYT19980206_0466__ei519,e_NYT19980206_0466__ei523,eq).
rel(e_NYT19980206_0466__ei534,e_NYT19980206_0466__ei525,gt).
rel(e_NYT19980206_0466__ei525,e_NYT19980206_0466__ei534,lt).
rel(e_NYT19980206_0466__ei534,e_NYT19980206_0466__ei519,gt).
rel(e_NYT19980206_0466__ei519,e_NYT19980206_0466__ei534,lt).
rel(e_NYT19980206_0466__ei534,e_NYT19980206_0466__ei526,gt).
rel(e_NYT19980206_0466__ei526,e_NYT19980206_0466__ei534,lt).

% --- query: intersect every e_NYT19980206_0466__ei523->M->e_NYT19980206_0466__ei534 length-2 composition ---
% path-consistency narrowing: the certified query relation is the SET of
% distinct composed relations; a singleton => ANSWER, >=2 (conflicting
% compositions => empty intersection) or 0 (no path) => ABSTAIN (Mode-B).
path_comp(e_NYT19980206_0466__ei523,e_NYT19980206_0466__ei534,R) :- rel(e_NYT19980206_0466__ei523,M,R1), rel(M,e_NYT19980206_0466__ei534,R2), comp(R1,R2,R).

% main computes the narrowed set Rs and PRINTS A VERDICT (end-to-end proof).
main :-
    ( setof(R, path_comp(e_NYT19980206_0466__ei523,e_NYT19980206_0466__ei534,R), Rs) ->
        ( Rs = [Single] ->
            format('PATHS: ~w~n', [Rs]),
            format('VERDICT: ANSWER(~w)~n', [Single])
        ; format('PATHS: ~w~n', [Rs]),
          write('VERDICT: ABSTAIN(conflict->empty-intersection->Mode-B)'), nl
        )
    ; write('PATHS: none'), nl,
      write('VERDICT: ABSTAIN(underdetermined-no-length2-path)'), nl
    ),
    halt.

:- initialization(main).
