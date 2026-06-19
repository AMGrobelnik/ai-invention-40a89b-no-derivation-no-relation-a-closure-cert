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
rel(e_CNN19980213_2130_0155__ei617,e_CNN19980213_2130_0155__ei633,lt).
rel(e_CNN19980213_2130_0155__ei633,e_CNN19980213_2130_0155__ei617,gt).

% --- query: intersect every e_CNN19980213_2130_0155__ei592->M->e_CNN19980213_2130_0155__ei617 composition ---
path_comp(e_CNN19980213_2130_0155__ei592,e_CNN19980213_2130_0155__ei617,R) :- rel(e_CNN19980213_2130_0155__ei592,M,R1), rel(M,e_CNN19980213_2130_0155__ei617,R2), comp(R1,R2,R).
main :- ( setof(R, path_comp(e_CNN19980213_2130_0155__ei592,e_CNN19980213_2130_0155__ei617,R), Rs) -> format('PATHS: ~w~n',[Rs]) ; write('PATHS: none'), nl ), halt.

:- initialization(main).
