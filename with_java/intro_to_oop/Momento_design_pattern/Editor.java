
/**
 * This is a implememtation of the momento
 * pattern that gives you the ability
 * to undo 
 * 
 * @author Tanvir
 * @version (a version number or a date)
 */
public class Editor
{
    // this class actually take the content 
    // and we can get and set the content
    private String content;
    
    // getter
    public String getContent(){
        return content;
    }
    // setter
    public void setContent(String content){
        this.content = content;
    } 
    
    
    
    // Editor class need the method to set content 
    // to the EditorState
    // and get content from the editorstate
    
    public EditorState createState(){
        // it will save and return the state
        return new EditorState(content);
    }
    
    
    // restore method
    // in the restore method we give  a state and it returns
    // the content of the state
    public void restore(EditorState state){
        content = state.getContent();
    }
    
    
    
    
    
    
    
}
