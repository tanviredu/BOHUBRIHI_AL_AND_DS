
/**
 * Write a description of class Canvas here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class Canvas
{
    private Tool currentTool;
    
    // make a getter and setter for
    // getting and setting tool
    // this currenttool have to be an object
    // whose class is implementted with tool
    
    // getter
    public Tool GetTool(){
        return currentTool;
    }
    
    public void setTool(Tool currentTool){
           this.currentTool = currentTool;
    }

    // remember this function name is done for mathcing
    // its implemeting anything
    public void mouseDown(){
        // the mouseDown of the current tool that is inherited from
        // the tool
        // its dependency injection
        currentTool.mouseDown();
    
    }
    
    public void mouseUp(){
        // the mouseUp of the current tool that is inherited from
        // the tool
        // its dependency injection
        currentTool.mouseUp();
    
    }

}
