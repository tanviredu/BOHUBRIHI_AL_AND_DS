
/**
 * Write a description of class History here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
import java.util.*;
public class History
{
    private ArrayList<EditorState> states = new ArrayList<EditorState>();
    
    public void push(EditorState state){
        states.add(state);
    }
    
    public EditorState pop(){
        var lastindex = states.size() -1;
        var laststate = states.get(lastindex);
        states.remove(laststate);
        return laststate;
    }
   
}
