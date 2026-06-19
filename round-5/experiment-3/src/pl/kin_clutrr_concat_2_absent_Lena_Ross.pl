% Closure-certified kinship deduction -- forward-union least-fixpoint trace program.
% der(A,T,B): T derivable for the directed pair A->B; closed under the finite
% composition table comp/3 + total converse conv/2 (both-direction seeding).
:- dynamic der/3.
% ---- composition rules comp(T1,T2,T3) ----
comp('child','child','grand').
comp('child','SO','in-law').
comp('child','sibling','child').
comp('child','inv-un','sibling').
comp('child','inv-grand','inv-child').
comp('inv-child','child','sibling').
comp('inv-child','inv-child','inv-grand').
comp('inv-child','sibling','inv-un').
comp('SO','inv-child','inv-in-law').
comp('SO','grand','grand').
comp('SO','child','child').
comp('sibling','sibling','sibling').
comp('sibling','inv-grand','inv-grand').
comp('sibling','child','un').
comp('sibling','inv-child','inv-child').
comp('grand','sibling','grand').
% ---- total converse conv(T,Tc) ----
conv('child','inv-child').
conv('inv-child','child').
conv('SO','SO').
conv('sibling','sibling').
conv('grand','inv-grand').
conv('inv-grand','grand').
conv('in-law','inv-in-law').
conv('inv-in-law','in-law').
conv('sibling-in-law','sibling-in-law').
conv('un','inv-un').
conv('inv-un','un').
% ---- seed: extracted atomic edges seed(A,T,B) ----
seed('David','sibling','Julie').
seed('Bonnie','child','Julie').
seed('Erica','child','Ross').
seed('Erica','sibling','Clifton').
seed('Ross','sibling','Patrick').
seed('Clifton','child','David').
seed('Arlene','inv-un','Melanie').
seed('Samuel','sibling','Melanie').
seed('Nancy','inv-child','Samuel').
seed('Milton','child','Arlene').
seed('Milton','inv-child','Antonia').
seed('Lilly','inv-child','Alvin').
seed('Alvin','child','Seth').
seed('Lilly','inv-child','Dorothy').
seed('Robert','sibling','Dorothy').
seed('Alvin','child','Warren').
seed('Andrew','inv-grand','Jose').
seed('Jeremy','inv-child','Victoria').
seed('Jeremy','sibling','Charles').
seed('Victoria','child','Richard').
seed('Richard','sibling','Andrew').
seed('Shantel','child','Beverly').
seed('Beverly','inv-child','Harold').
seed('Pedro','inv-child','Shantel').
seed('Pedro','child','Rebecca').
seed('Tina','inv-un','Francisco').
seed('Frances','child','Lena').
seed('Lena','child','Tina').
% ---- add a directed edge + its converse (idempotent) ----
add_edge(A,T,B) :- ( der(A,T,B) -> true ; assertz(der(A,T,B)) ),
                   conv(T,Tc), ( der(B,Tc,A) -> true ; assertz(der(B,Tc,A)) ).
init_seed :- forall(seed(A,T,B), add_edge(A,T,B)).
% ---- batch forward-chaining to least fixpoint ----
one_pass :- findall(d(A,T3,C),
             ( der(A,T1,B), der(B,T2,C), comp(T1,T2,T3), \+ der(A,T3,C) ), L0),
           sort(L0, L), ( L == [] -> true
             ; ( forall(member(d(A,T,C),L), add_edge(A,T,C)), one_pass ) ).
run :- init_seed, one_pass,
       ( setof(R, der('Lena',R,'Ross'), Rs) -> true ; Rs = [] ),
       forall(member(R,Rs), (write('RESULT:'), write(R), nl)), halt.
:- initialization(run).
