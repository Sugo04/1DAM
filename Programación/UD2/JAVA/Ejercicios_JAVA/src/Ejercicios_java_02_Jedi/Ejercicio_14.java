/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Ejercicios_java_02_Jedi;

/**
 *
 * @author usuario
 */
//Importamos el java.util.Scanner
import java.util.Scanner;
public class Ejercicio_14 {
    
    public static void main (String[] args){
        
        //Declaramos nuestras variables
        
        double num1, num2;
        
        //Introducimos lector y entrada como scanners.
         Scanner lector = new Scanner(System.in);
         
        
        /**
         * Mostramos en pantalla un mensaje para indicar que deberán de hacer.
         */
        
        System.out.println("Ahora deberá de introducir dos números (pueden"
                + "tener decimales");
        
        /**
         * Indicaré con un mensaje donde deberá de introducir cada uno de los 
         * números requeridos para el ejercicio, así como introduciré los 
         * lectores.
         */
        
        System.out.println("Introduzca el primer número: ");
        
        num1 = lector.nextDouble();
        
        System.out.println("Introduzca el segundo número:  ");
        
        num2 = lector.nextDouble();
        
        /**
         * Ahora realizaremos el condicionante necesario, para comprobar cual 
         * de sendos números es mayor, y devolver con un mensaje en la pantalla
         * la solución.
         */
        
        if (num1>num2) 
        {
            System.out.println("El mayor es: "+num1);   
        } 
        else 
        {
            if (num1==num2) {
                System.out.println("Son iguales");
            }
            
        }
      
    
    
    }
    
}
