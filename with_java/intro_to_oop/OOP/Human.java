
/**
 * Write a description of class Human here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class Human
{
    String name;
    int age;
    int heightinInches;
    String eyeColor;
    
    // this is the constructor method
    public Human(String name,int heightinInches,String eyeColor){
        this.name = name;
        this.heightinInches = heightinInches;
        this.eyeColor = eyeColor;
        
    
    }
    
    public void speak(){
        System.out.println("Hello my name is "+name);
        System.out.println("I am "+heightinInches+"inch tall");
        System.out.println("My Eye color "+eyeColor);
        
    }
    
    
    public void eat(){
        System.out.println("Eating.......");
        
    }
    
    public void walk(){
        System.out.println("Working........");
    
    }
    
}
