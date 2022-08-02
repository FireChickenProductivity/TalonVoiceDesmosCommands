title: /Desmos/
-
#square root command
[square] root [of]: 'sqrt'

#inserts plus
plus: '+'

#inserts minus sign
minus|negative: '-'

#insert a slash
slash: '/'

#inserts multiplication symbol
times: '*'
#inserts a small number followed by the multiplication symbol
# needed to override a community repository repeating command
<number_small> times: 
    user.desmos_insert_small_number(number_small)
    insert('*')

#open parentheses
[open|left] paren: '('
#close parenthesis
(close|right) paren: ')'

#reference the previous answer
ans|answer: 'ans'