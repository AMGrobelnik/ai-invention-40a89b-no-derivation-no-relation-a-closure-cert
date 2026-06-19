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
rel(e_CNN19980213_2130_0155__ei575,e_CNN19980213_2130_0155__ei607,lt).
rel(e_CNN19980213_2130_0155__ei607,e_CNN19980213_2130_0155__ei575,gt).
rel(e_CNN19980213_2130_0155__ei575,e_CNN19980213_2130_0155__ei628,lt).
rel(e_CNN19980213_2130_0155__ei628,e_CNN19980213_2130_0155__ei575,gt).
rel(e_CNN19980213_2130_0155__ei624,e_CNN19980213_2130_0155__ei607,gt).
rel(e_CNN19980213_2130_0155__ei607,e_CNN19980213_2130_0155__ei624,lt).
rel(e_CNN19980213_2130_0155__ei624,e_CNN19980213_2130_0155__ei628,lt).
rel(e_CNN19980213_2130_0155__ei628,e_CNN19980213_2130_0155__ei624,gt).
rel(e_CNN19980213_2130_0155__ei624,e_CNN19980213_2130_0155__ei604,gt).
rel(e_CNN19980213_2130_0155__ei604,e_CNN19980213_2130_0155__ei624,lt).
rel(e_CNN19980213_2130_0155__ei607,e_CNN19980213_2130_0155__ei628,lt).
rel(e_CNN19980213_2130_0155__ei628,e_CNN19980213_2130_0155__ei607,gt).
rel(e_CNN19980213_2130_0155__ei607,e_CNN19980213_2130_0155__ei604,gt).
rel(e_CNN19980213_2130_0155__ei604,e_CNN19980213_2130_0155__ei607,lt).
rel(e_CNN19980213_2130_0155__ei628,e_CNN19980213_2130_0155__ei604,gt).
rel(e_CNN19980213_2130_0155__ei604,e_CNN19980213_2130_0155__ei628,lt).

% --- query: intersect every e_CNN19980213_2130_0155__ei575->M->e_CNN19980213_2130_0155__ei624 composition ---
path_comp(e_CNN19980213_2130_0155__ei575,e_CNN19980213_2130_0155__ei624,R) :- rel(e_CNN19980213_2130_0155__ei575,M,R1), rel(M,e_CNN19980213_2130_0155__ei624,R2), comp(R1,R2,R).
main :- ( setof(R, path_comp(e_CNN19980213_2130_0155__ei575,e_CNN19980213_2130_0155__ei624,R), Rs) -> format('PATHS: ~w~n',[Rs]) ; write('PATHS: none'), nl ), halt.

:- initialization(main).
