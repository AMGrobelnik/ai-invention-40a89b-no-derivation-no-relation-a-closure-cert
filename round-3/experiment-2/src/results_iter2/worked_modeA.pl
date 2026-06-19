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
rel(e_ea980120_1830_0456__ei107,e_ea980120_1830_0456__ei104,lt).
rel(e_ea980120_1830_0456__ei104,e_ea980120_1830_0456__ei107,gt).
rel(e_ea980120_1830_0456__ei107,e_ea980120_1830_0456__ei102,gt).
rel(e_ea980120_1830_0456__ei102,e_ea980120_1830_0456__ei107,lt).
rel(e_ea980120_1830_0456__ei107,e_ea980120_1830_0456__ei109,lt).
rel(e_ea980120_1830_0456__ei109,e_ea980120_1830_0456__ei107,gt).
rel(e_ea980120_1830_0456__ei110,e_ea980120_1830_0456__ei102,gt).
rel(e_ea980120_1830_0456__ei102,e_ea980120_1830_0456__ei110,lt).
rel(e_ea980120_1830_0456__ei110,e_ea980120_1830_0456__ei109,gt).
rel(e_ea980120_1830_0456__ei109,e_ea980120_1830_0456__ei110,lt).

% --- query: intersect every e_ea980120_1830_0456__ei107->M->e_ea980120_1830_0456__ei110 composition ---
path_comp(e_ea980120_1830_0456__ei107,e_ea980120_1830_0456__ei110,R) :- rel(e_ea980120_1830_0456__ei107,M,R1), rel(M,e_ea980120_1830_0456__ei110,R2), comp(R1,R2,R).
main :- ( setof(R, path_comp(e_ea980120_1830_0456__ei107,e_ea980120_1830_0456__ei110,R), Rs) -> format('PATHS: ~w~n',[Rs]) ; write('PATHS: none'), nl ), halt.

:- initialization(main).
