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
rel(e_CNN19980213_2130_0155__ei586,e_CNN19980213_2130_0155__ei599,lt).
rel(e_CNN19980213_2130_0155__ei599,e_CNN19980213_2130_0155__ei586,gt).
rel(e_CNN19980213_2130_0155__ei637,e_CNN19980213_2130_0155__ei634,gt).
rel(e_CNN19980213_2130_0155__ei634,e_CNN19980213_2130_0155__ei637,lt).
rel(e_CNN19980213_2130_0155__ei599,e_CNN19980213_2130_0155__ei573,gt).
rel(e_CNN19980213_2130_0155__ei573,e_CNN19980213_2130_0155__ei599,lt).
rel(e_CNN19980213_2130_0155__ei599,e_CNN19980213_2130_0155__ei634,lt).
rel(e_CNN19980213_2130_0155__ei634,e_CNN19980213_2130_0155__ei599,gt).
rel(e_CNN19980213_2130_0155__ei573,e_CNN19980213_2130_0155__ei634,lt).
rel(e_CNN19980213_2130_0155__ei634,e_CNN19980213_2130_0155__ei573,gt).

% --- query: intersect every e_CNN19980213_2130_0155__ei586->M->e_CNN19980213_2130_0155__ei637 composition ---
path_comp(e_CNN19980213_2130_0155__ei586,e_CNN19980213_2130_0155__ei637,R) :- rel(e_CNN19980213_2130_0155__ei586,M,R1), rel(M,e_CNN19980213_2130_0155__ei637,R2), comp(R1,R2,R).
main :- ( setof(R, path_comp(e_CNN19980213_2130_0155__ei586,e_CNN19980213_2130_0155__ei637,R), Rs) -> format('PATHS: ~w~n',[Rs]) ; write('PATHS: none'), nl ), halt.

:- initialization(main).
