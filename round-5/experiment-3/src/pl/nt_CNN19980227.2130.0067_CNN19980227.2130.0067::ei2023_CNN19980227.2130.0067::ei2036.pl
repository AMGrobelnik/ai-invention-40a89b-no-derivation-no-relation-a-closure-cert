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
rel(e_CNN19980227_2130_0067__ei2023,e_CNN19980227_2130_0067__ei2047,lt).
rel(e_CNN19980227_2130_0067__ei2047,e_CNN19980227_2130_0067__ei2023,gt).
rel(e_CNN19980227_2130_0067__ei2036,e_CNN19980227_2130_0067__ei2047,lt).
rel(e_CNN19980227_2130_0067__ei2047,e_CNN19980227_2130_0067__ei2036,gt).
rel(e_CNN19980227_2130_0067__ei2036,e_CNN19980227_2130_0067__ei2007,gt).
rel(e_CNN19980227_2130_0067__ei2007,e_CNN19980227_2130_0067__ei2036,lt).
rel(e_CNN19980227_2130_0067__ei2036,e_CNN19980227_2130_0067__ei2008,gt).
rel(e_CNN19980227_2130_0067__ei2008,e_CNN19980227_2130_0067__ei2036,lt).
rel(e_CNN19980227_2130_0067__ei2007,e_CNN19980227_2130_0067__ei2008,eq).
rel(e_CNN19980227_2130_0067__ei2008,e_CNN19980227_2130_0067__ei2007,eq).

% --- query: intersect every e_CNN19980227_2130_0067__ei2023->M->e_CNN19980227_2130_0067__ei2036 composition ---
path_comp(e_CNN19980227_2130_0067__ei2023,e_CNN19980227_2130_0067__ei2036,R) :- rel(e_CNN19980227_2130_0067__ei2023,M,R1), rel(M,e_CNN19980227_2130_0067__ei2036,R2), comp(R1,R2,R).
main :- ( setof(R, path_comp(e_CNN19980227_2130_0067__ei2023,e_CNN19980227_2130_0067__ei2036,R), Rs) -> format('PATHS: ~w~n',[Rs]) ; write('PATHS: none'), nl ), halt.

:- initialization(main).
