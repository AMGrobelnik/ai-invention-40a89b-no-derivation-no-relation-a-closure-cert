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
rel(e_APW19980213_1310__ei2015,e_APW19980213_1310__ei2007,gt).
rel(e_APW19980213_1310__ei2007,e_APW19980213_1310__ei2015,lt).
rel(e_APW19980213_1310__ei2015,e_APW19980213_1310__ei2047,lt).
rel(e_APW19980213_1310__ei2047,e_APW19980213_1310__ei2015,gt).
rel(e_APW19980213_1310__ei2038,e_APW19980213_1310__ei2007,gt).
rel(e_APW19980213_1310__ei2007,e_APW19980213_1310__ei2038,lt).
rel(e_APW19980213_1310__ei2038,e_APW19980213_1310__ei2024,gt).
rel(e_APW19980213_1310__ei2024,e_APW19980213_1310__ei2038,lt).
rel(e_APW19980213_1310__ei2038,e_APW19980213_1310__ei2047,lt).
rel(e_APW19980213_1310__ei2047,e_APW19980213_1310__ei2038,gt).
rel(e_APW19980213_1310__ei2007,e_APW19980213_1310__ei2047,lt).
rel(e_APW19980213_1310__ei2047,e_APW19980213_1310__ei2007,gt).
rel(e_APW19980213_1310__ei2024,e_APW19980213_1310__ei2047,lt).
rel(e_APW19980213_1310__ei2047,e_APW19980213_1310__ei2024,gt).

% --- query: intersect every e_APW19980213_1310__ei2015->M->e_APW19980213_1310__ei2038 composition ---
path_comp(e_APW19980213_1310__ei2015,e_APW19980213_1310__ei2038,R) :- rel(e_APW19980213_1310__ei2015,M,R1), rel(M,e_APW19980213_1310__ei2038,R2), comp(R1,R2,R).
main :- ( setof(R, path_comp(e_APW19980213_1310__ei2015,e_APW19980213_1310__ei2038,R), Rs) -> format('PATHS: ~w~n',[Rs]) ; write('PATHS: none'), nl ), halt.

:- initialization(main).
