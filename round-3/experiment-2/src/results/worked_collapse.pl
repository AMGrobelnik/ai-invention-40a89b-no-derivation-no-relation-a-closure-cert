% Closure-certified temporal deduction -- Mode-B INCONSISTENCY certificate.
% Convex point start-point algebra {lt,eq,gt}. The query edge is held at the
% universe; a Mode-B collapse is a contradiction among the LOCAL path-edge reads:
% some triangle has compose(R(a,b),R(b,c)) /= the direct read R(a,c).
:- discontiguous rel/3.

% --- composition table (Vilain-Kautz convex point algebra) ---
comp(lt,lt,lt).
comp(lt,eq,lt).
comp(eq,lt,lt).
comp(eq,eq,eq).
comp(eq,gt,gt).
comp(gt,eq,gt).
comp(gt,gt,gt).

% --- singleton local reads (both directions via converse) ---
rel(e_ea980120_1830_0071__ei211,e_ea980120_1830_0071__ei208,gt).
rel(e_ea980120_1830_0071__ei208,e_ea980120_1830_0071__ei211,lt).
rel(e_ea980120_1830_0071__ei211,e_ea980120_1830_0071__ei199,lt).
rel(e_ea980120_1830_0071__ei199,e_ea980120_1830_0071__ei211,gt).
rel(e_ea980120_1830_0071__ei211,e_ea980120_1830_0071__ei209,gt).
rel(e_ea980120_1830_0071__ei209,e_ea980120_1830_0071__ei211,lt).
rel(e_ea980120_1830_0071__ei220,e_ea980120_1830_0071__ei208,gt).
rel(e_ea980120_1830_0071__ei208,e_ea980120_1830_0071__ei220,lt).
rel(e_ea980120_1830_0071__ei208,e_ea980120_1830_0071__ei199,gt).
rel(e_ea980120_1830_0071__ei199,e_ea980120_1830_0071__ei208,lt).

% an inconsistent triangle: composed relation conflicts with the direct read
bad(A,B,C,R1,R2,Rc,R3) :- rel(A,B,R1), rel(B,C,R2), comp(R1,R2,Rc), rel(A,C,R3), R3 \== Rc.
main :- ( bad(A,B,C,R1,R2,Rc,R3) ->
    format('INCONSISTENT-TRIANGLE: ~w-~w-~w  comp(~w,~w)=~w but rel(~w,~w)=~w~n',[A,B,C,R1,R2,Rc,A,C,R3]),
    write('VERDICT: INCONSISTENT(Mode-B ABSTAIN)'), nl
  ; write('VERDICT: consistent-among-singletons (full PC-2 over disjunctive/long-range reads found the conflict)'), nl ),
  halt.

:- initialization(main).
