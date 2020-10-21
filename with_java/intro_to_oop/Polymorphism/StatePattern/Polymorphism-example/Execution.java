
/**
 * Write a description of class Execution here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class Execution
{
    public static void main(String[] args){
        
        // this method takes object
        // that implements/extends the UIControl
        // class
        drawUIControl(new TextBox());
        drawUIControl(new CheckBox());
        
    
    }
    
    private static void drawUIControl(UIControl control){
        control.draw();
        
    
    }
}
