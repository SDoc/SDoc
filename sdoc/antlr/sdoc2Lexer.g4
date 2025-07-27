lexer grammar sdoc2Lexer;

// Default mode TEXT.
TEXT
  : ~[\\]+
  | '\\\\';

// SDoc2 keywords
BEGIN:      '\\begin'    -> pushMode(MODE_BLOCK);
END:        '\\end'      -> pushMode(MODE_BLOCK);

POSITION:   '\\position' {pass} -> pushMode(MODE_ARGS);

// All other tokens starting with \ are considered SDoc2 line commands.
SDOC2_COMMAND: '\\'[a-z_][a-z0-9_]*  -> pushMode(MODE_ARGS);


mode MODE_BLOCK;

BLOCK_LEFT_BRACKET: '['  -> pushMode(MODE_OPT_ARGS);
BLOCK_LEFT_BRACE:   '{'  -> pushMode(MODE_BLOCK_NAME);
BLOCK_WS: [ \t\r\n]+ -> skip;

// Mode for the name of a block SDoc2 command.
mode MODE_BLOCK_NAME;

BLOCK_RIGHT_BRACE:  '}'[ \t\r\n]*  -> popMode,popMode;

BLOCK_ARG_ARG: (~[{}] | '\\'. )+;

// Mode for SDoc2 commands with an argument, i.e. \chapter{What is SDoc?}
mode MODE_ARGS;

OPT_ARGS_LEFT_BRACKET: '['  -> pushMode(MODE_OPT_ARGS);
MAIN_ARG_LEFT_BRACE:   '{'  -> pushMode(MODE_MAIN_ARG);


// Mode for optinal arguments.
mode MODE_OPT_ARGS;

OPT_ARGS_RIGHT_BRACKET: ']'  -> popMode;
OPT_ARGS_EQUALS:        '=';
OPT_ARGS_SEPARATOR:     ' ';

OPT_ARGS_NAME: [a-zA-Z][a-zA-Z0-9_]*;

OPT_ARGS_VALUE
   : OPT_ARGS_STRING
   | OPT_ARGS_INT
   ;

fragment
OPT_ARGS_STRING
   :   '"' ~["]* '"'
   |   '\'' ~[']* '\''
   ;

fragment
OPT_ARGS_INT: [0-9]+;

OPT_ARGS_WS: [ \t\r\n]+ -> skip ;


// Mode for main argument.
mode MODE_MAIN_ARG;

MAIN_ARG_RIGHT_BRACE:  '}'  -> popMode,popMode;

MAIN_ARG: (~[{}] | '\\'. )+;
