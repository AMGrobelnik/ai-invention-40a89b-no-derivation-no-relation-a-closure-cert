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
rel(e_APW19980213_1310__ei2040,e_APW19980213_1310__ei2001,gt).
rel(e_APW19980213_1310__ei2001,e_APW19980213_1310__ei2040,lt).
rel(e_APW19980213_1310__ei2040,e_APW19980213_1310__ei2007,gt).
rel(e_APW19980213_1310__ei2007,e_APW19980213_1310__ei2040,lt).
rel(e_APW19980213_1310__ei2056,e_APW19980213_1310__ei2001,lt).
rel(e_APW19980213_1310__ei2001,e_APW19980213_1310__ei2056,gt).
rel(e_APW19980213_1310__ei2056,e_APW19980213_1310__ei2007,lt).
rel(e_APW19980213_1310__ei2007,e_APW19980213_1310__ei2056,gt).
rel(e_APW19980213_1310__ei2056,e_APW19980213_1310__ei2067,lt).
rel(e_APW19980213_1310__ei2067,e_APW19980213_1310__ei2056,gt).
rel(e_APW19980213_1310__ei2001,e_APW19980213_1310__ei2007,eq).
rel(e_APW19980213_1310__ei2007,e_APW19980213_1310__ei2001,eq).
rel(e_APW19980213_1310__ei2007,e_APW19980213_1310__ei2067,lt).
rel(e_APW19980213_1310__ei2067,e_APW19980213_1310__ei2007,gt).

% --- query: intersect every e_APW19980213_1310__ei2040->M->e_APW19980213_1310__ei2056 composition ---
path_comp(e_APW19980213_1310__ei2040,e_APW19980213_1310__ei2056,R) :- rel(e_APW19980213_1310__ei2040,M,R1), rel(M,e_APW19980213_1310__ei2056,R2), comp(R1,R2,R).
main :- ( setof(R, path_comp(e_APW19980213_1310__ei2040,e_APW19980213_1310__ei2056,R), Rs) -> format('PATHS: ~w~n',[Rs]) ; write('PATHS: none'), nl ), halt.

:- initialization(main).
