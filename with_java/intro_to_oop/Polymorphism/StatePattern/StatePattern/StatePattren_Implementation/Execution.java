
/**
 * Write a description of class Execution here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class Execution
{
   
    public static void main(String[] args){
        var canvas = new Canvas();
        canvas.setTool(new SelectionTool());
        canvas.mouseDown();
        canvas.mouseUp();
        canvas.setTool(new BrushTool());
        canvas.mouseDown();
        canvas.mouseUp();
        
    }
}
