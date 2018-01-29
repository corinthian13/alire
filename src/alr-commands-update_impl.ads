package Alr.Commands.Update_Impl is

   type Command is new Commands.Command with null record;

   overriding procedure Execute (Cmd : in out Command);

   overriding procedure Setup_Switches (Cmd    : in out Command;
                                        Config : in out GNAT.Command_Line.Command_Line_Configuration) is null;

   overriding function Short_Description (Cmd : Command) return String is
      ("Fetches the latest alr executable package index.");

   overriding function Usage_Custom_Parameters (Cmd : Command) return String is ("");

end Alr.Commands.Update_Impl;
