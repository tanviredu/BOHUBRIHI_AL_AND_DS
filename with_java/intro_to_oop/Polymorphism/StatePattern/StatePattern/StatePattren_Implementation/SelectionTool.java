
/**
 * Write a description of class SelectionTool here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class SelectionTool implements Tool
{
    @Override
    public void mouseDown(){
        System.out.println("Changed into Seletion Icon");
    }
    
    @Override
    public void mouseUp(){
        System.out.println("Draw Rectangle");
        
    }
   
}
