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

% --- query: intersect every e_ABC19980108_1830_0711__ei375->M->e_ABC19980108_1830_0711__ei433 composition ---
path_comp(e_ABC19980108_1830_0711__ei375,e_ABC19980108_1830_0711__ei433,R) :- rel(e_ABC19980108_1830_0711__ei375,M,R1), rel(M,e_ABC19980108_1830_0711__ei433,R2), comp(R1,R2,R).
main :- ( setof(R, path_comp(e_ABC19980108_1830_0711__ei375,e_ABC19980108_1830_0711__ei433,R), Rs) -> format('PATHS: ~w~n',[Rs]) ; write('PATHS: none'), nl ), halt.

:- initialization(main).
