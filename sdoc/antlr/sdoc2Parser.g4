parser grammar sdoc2Parser;

options { tokenVocab=sdoc2Lexer; }

sdoc: (command|text)*;

text: TEXT;

// All SDoc2 commands.
command
  : cmd_begin
  | cmd_end
  | cmd_position

  | cmd_sdoc2   // Note: This command MUST be the last alternative of all commands.
  ;

// Begin command. Start a block command, e.g. \begin{itemize}
cmd_begin:
   BEGIN
   (BLOCK_LEFT_BRACKET (OPT_ARGS_NAME OPT_ARGS_EQUALS OPT_ARGS_VALUE)?
                        (OPT_ARGS_SEPARATOR OPT_ARGS_NAME OPT_ARGS_EQUALS OPT_ARGS_VALUE)*
                        OPT_ARGS_SEPARATOR?  OPT_ARGS_RIGHT_BRACKET)?
   BLOCK_LEFT_BRACE BLOCK_ARG_ARG BLOCK_RIGHT_BRACE;

// End command. The end of a block command, e.g. \end{itemize}
cmd_end: END BLOCK_LEFT_BRACE BLOCK_ARG_ARG BLOCK_RIGHT_BRACE;

// SDoc2 command position
cmd_position:
    POSITION MAIN_ARG_LEFT_BRACE MAIN_ARG MAIN_ARG_RIGHT_BRACE;

// Other SDoc2 commands.
cmd_sdoc2:
    SDOC2_COMMAND
    (OPT_ARGS_LEFT_BRACKET (OPT_ARGS_NAME OPT_ARGS_EQUALS OPT_ARGS_VALUE)?
                             (OPT_ARGS_SEPARATOR OPT_ARGS_NAME OPT_ARGS_EQUALS OPT_ARGS_VALUE)*
                              OPT_ARGS_SEPARATOR? OPT_ARGS_RIGHT_BRACKET)?
    (MAIN_ARG_LEFT_BRACE MAIN_ARG? MAIN_ARG_RIGHT_BRACE)?;
