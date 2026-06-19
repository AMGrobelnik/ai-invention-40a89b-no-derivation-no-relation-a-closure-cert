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
rel(e_APW19980213_1310__ei2028,e_APW19980213_1310__ei2038,lt).
rel(e_APW19980213_1310__ei2038,e_APW19980213_1310__ei2028,gt).
rel(e_APW19980213_1310__ei2028,e_APW19980213_1310__ei2077,gt).
rel(e_APW19980213_1310__ei2077,e_APW19980213_1310__ei2028,lt).
rel(e_APW19980213_1310__ei2038,e_APW19980213_1310__ei2077,gt).
rel(e_APW19980213_1310__ei2077,e_APW19980213_1310__ei2038,lt).
rel(e_APW19980213_1310__ei2038,e_APW19980213_1310__ei2047,lt).
rel(e_APW19980213_1310__ei2047,e_APW19980213_1310__ei2038,gt).
rel(e_APW19980213_1310__ei2077,e_APW19980213_1310__ei2047,lt).
rel(e_APW19980213_1310__ei2047,e_APW19980213_1310__ei2077,gt).

% --- query: intersect every e_APW19980213_1310__ei2028->M->e_APW19980213_1310__ei2074 composition ---
path_comp(e_APW19980213_1310__ei2028,e_APW19980213_1310__ei2074,R) :- rel(e_APW19980213_1310__ei2028,M,R1), rel(M,e_APW19980213_1310__ei2074,R2), comp(R1,R2,R).
main :- ( setof(R, path_comp(e_APW19980213_1310__ei2028,e_APW19980213_1310__ei2074,R), Rs) -> format('PATHS: ~w~n',[Rs]) ; write('PATHS: none'), nl ), halt.

:- initialization(main).
