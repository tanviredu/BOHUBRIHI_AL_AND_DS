import java.util.*;

/**
 * Write a description of interface IPersonRepository here.
 *
 * @author Tanvir
 * @version (a version number or a date)
 */
public interface IPersonRepository
{
    ArrayList<Person>getPeople();
    Person GetPerson(int id);
    void AddPerson(Person newPerson);
    void DeletePerson(int id);
    Person UpdatePerson(int id,Person updatedPerson);
    
    
}
