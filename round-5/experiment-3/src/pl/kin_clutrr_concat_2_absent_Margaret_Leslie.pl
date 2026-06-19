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
seed('Roger','sibling','Earline').
seed('Manuel','child','Roger').
seed('Mary','inv-child','Manuel').
seed('Alice','child','Kim').
seed('Kim','sibling','Roger').
seed('Manuel','child','Mary').
seed('Manuel','child','Kim').
seed('Earline','sibling','Kim').
seed('Kyle','child','Albert').
seed('Susan','child','Betty').
seed('Bonita','child','Albert').
seed('Albert','sibling','Maryann').
seed('Frank','sibling','Maryann').
seed('Susan','un','Bryan').
seed('John','sibling','Kyle').
seed('Albert','sibling','Frank').
seed('Steve','child','Steven').
seed('William','sibling','Cesar').
seed('William','sibling','Constance').
seed('Constance','child','Beatrice').
seed('Ellen','sibling','Margaret').
seed('Margaret','child','Sharon').
seed('Margaret','inv-child','Steven').
seed('Kathleen','sibling','Sharon').
seed('Mabel','sibling','Kathleen').
seed('Steve','child','Beatrice').
seed('Marguerite','child','Jerry').
seed('Peter','inv-un','Marguerite').
seed('Bertha','sibling','Peter').
seed('Alfred','inv-child','Stephen').
seed('Jennifer','child','Bertha').
seed('Jerry','inv-un','Carlos').
seed('Mark','sibling','Ronald').
seed('Milton','sibling','Loren').
seed('Santa','sibling','Milton').
seed('Helen','sibling','Wallace').
seed('Wallace','inv-child','Mark').
seed('Milton','child','Ronald').
seed('Marie','inv-child','Donna').
seed('Marie','sibling','Helen').
seed('Loren','sibling','Milton').
seed('Jeffery','sibling','Leslie').
seed('Richard','sibling','Leslie').
seed('Richard','inv-child','Maria').
seed('Richard','sibling','Lucas').
seed('James','child','Jeffery').
seed('James','sibling','Donald').
seed('Leslie','sibling','Lucas').
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
       ( setof(R, der('Margaret',R,'Leslie'), Rs) -> true ; Rs = [] ),
       forall(member(R,Rs), (write('RESULT:'), write(R), nl)), halt.
:- initialization(run).
