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
rel(e_APW19980418_0210__ei2130,e_APW19980418_0210__ei2142,lt).
rel(e_APW19980418_0210__ei2142,e_APW19980418_0210__ei2130,gt).
rel(e_APW19980418_0210__ei2130,e_APW19980418_0210__ei2127,gt).
rel(e_APW19980418_0210__ei2127,e_APW19980418_0210__ei2130,lt).
rel(e_APW19980418_0210__ei2130,e_APW19980418_0210__ei2140,lt).
rel(e_APW19980418_0210__ei2140,e_APW19980418_0210__ei2130,gt).
rel(e_APW19980418_0210__ei2147,e_APW19980418_0210__ei2142,gt).
rel(e_APW19980418_0210__ei2142,e_APW19980418_0210__ei2147,lt).
rel(e_APW19980418_0210__ei2147,e_APW19980418_0210__ei2127,lt).
rel(e_APW19980418_0210__ei2127,e_APW19980418_0210__ei2147,gt).
rel(e_APW19980418_0210__ei2147,e_APW19980418_0210__ei2140,gt).
rel(e_APW19980418_0210__ei2140,e_APW19980418_0210__ei2147,lt).
rel(e_APW19980418_0210__ei2142,e_APW19980418_0210__ei2127,lt).
rel(e_APW19980418_0210__ei2127,e_APW19980418_0210__ei2142,gt).
rel(e_APW19980418_0210__ei2142,e_APW19980418_0210__ei2140,lt).
rel(e_APW19980418_0210__ei2140,e_APW19980418_0210__ei2142,gt).
rel(e_APW19980418_0210__ei2127,e_APW19980418_0210__ei2140,lt).
rel(e_APW19980418_0210__ei2140,e_APW19980418_0210__ei2127,gt).

% --- query: intersect every e_APW19980418_0210__ei2130->M->e_APW19980418_0210__ei2147 composition ---
path_comp(e_APW19980418_0210__ei2130,e_APW19980418_0210__ei2147,R) :- rel(e_APW19980418_0210__ei2130,M,R1), rel(M,e_APW19980418_0210__ei2147,R2), comp(R1,R2,R).
main :- ( setof(R, path_comp(e_APW19980418_0210__ei2130,e_APW19980418_0210__ei2147,R), Rs) -> format('PATHS: ~w~n',[Rs]) ; write('PATHS: none'), nl ), halt.

:- initialization(main).
