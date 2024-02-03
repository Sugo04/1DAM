/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Ejercicios_java2_02_Jedi;

/**
 *
 * @author usuario
 */
//importamos el java.util.scanner
import java.util.Scanner; 
public class Ejercicio_5 {
    public static void main(String[]args){
        
        //Definimos la variable que usaremos (un número)
        
        int num;
        
        // Declaramos el lector, o scanner
        Scanner lector = new Scanner(System.in);
        
        /** 
         * Mostramos en pantalla el mensaje que le dictará al usuario qué 
         * deberá de hacer.
         */
        
        System.out.println("A continuación usted deberá introducir "
                + "el número del que desea saber su factorial.");
        
        /** 
         * Agregamos otro mensaje a pantalla indicando el lugar donde debe
         * introducir el dato numérico.
         */
        
        System.out.println("Insrte el valor aquí: ");
        num = lector.nextInt();
        
        /**
         * declaramos un contador para el bucle que introduciremos para hayar 
         * la solución.
         */
         
        int i;
        i=1;
        
        while (num>1) {
            
            i=i*num;
            num = num-1;
                    
            
        }
        // ponemos un mensaje en pantalla con la solución
        
        System.out.println("El factorial de "+num+" es: "+i);
    
    }
}
