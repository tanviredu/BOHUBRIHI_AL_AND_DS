
/**
 * Write a description of class Execution here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class Execution
{
    public static void main(String[] args){
        var editor  = new Editor();
        var history = new History(); 
        editor.setContent("a");
        history.push(editor.createState()); // this will create and return a state that
                                            // we need to add it to the list
                              
        editor.setContent("b");
        history.push(editor.createState());
        editor.setContent("c");
        history.push(editor.createState());
        editor.setContent("d");
        System.out.println(editor.getContent());
        editor.restore(history.pop());
        System.out.println(editor.getContent());
        editor.restore(history.pop());
        System.out.println(editor.getContent());
    }
}
