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
rel(e_APW19980213_1310__ei2057,e_APW19980213_1310__ei2066,eq).
rel(e_APW19980213_1310__ei2066,e_APW19980213_1310__ei2057,eq).
rel(e_APW19980213_1310__ei2076,e_APW19980213_1310__ei2066,lt).
rel(e_APW19980213_1310__ei2066,e_APW19980213_1310__ei2076,gt).
rel(e_APW19980213_1310__ei2076,e_APW19980213_1310__ei2064,lt).
rel(e_APW19980213_1310__ei2064,e_APW19980213_1310__ei2076,gt).

% --- query: intersect every e_APW19980213_1310__ei2057->M->e_APW19980213_1310__ei2076 composition ---
path_comp(e_APW19980213_1310__ei2057,e_APW19980213_1310__ei2076,R) :- rel(e_APW19980213_1310__ei2057,M,R1), rel(M,e_APW19980213_1310__ei2076,R2), comp(R1,R2,R).
main :- ( setof(R, path_comp(e_APW19980213_1310__ei2057,e_APW19980213_1310__ei2076,R), Rs) -> format('PATHS: ~w~n',[Rs]) ; write('PATHS: none'), nl ), halt.

:- initialization(main).
