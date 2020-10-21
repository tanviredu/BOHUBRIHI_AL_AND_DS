
/**
 * Write a description of class BrushTool here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class BrushTool implements Tool
{
    @Override
    public void mouseDown(){
        System.out.println("Convert to Brush Icon");
    }

    @Override
    public void mouseUp(){
        System.out.println("Draw a line");
        
    }
}
