
/**
 * Write a description of class EditorState here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class EditorState
{
    private String content;
    
    // init the state with the constructor
    public EditorState(String content){
        this.content = content;
    }
    
    
    // we need getter for getting content from the 
    // Editor State
    public String getContent(){
        return content;
    }
    
}
