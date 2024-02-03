/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt 
 * to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java 
 * to edit this template
 */
package Ejercicios_java_02_Jedi;

/**
 * Alumno: Héctor Martín Ortega
 * 1º GS Desarrollo de Aplicaciones Multiplataforma
 * 
 * *************************ENUNCIADO*****************************************
 * Ejercicio_10: Escribe un programa que lee dos números, calcula y muestra el 
 * valor de su suma, resta, producto y división 
 * (Ten en cuenta la división por cero).
 * ***************************************************************************
 */

//Importamos java.util.Scanner
import java.util.Scanner;
public class Ejercicio_10 {
    
    public static void main (String[]args){
    
        //Definimos las variables que van a estar en el documento.
        int num1, num2, suma, resta, producto, division;
        
        //Introducimos lector como scanner.
        Scanner lector = new Scanner(System.in);
        
        
        /**
         * Ahora muestro en pantalla el mensaje que dirá que se introduzca el 
         * valor del num1 y num2.
         */
        
        System.out.println("Introduzca ambos numeros a continuación. ");
        
        /**
         * Para una mejor comprensión de donde se debe intoducir agregaré un 
         * mensaje junto al lector.
         * 
         */
        
        System.out.println("Primer número: "); 
        
        num1 = lector.nextInt();
        
        System.out.println("Segundo número:  ");
        
        num2 = lector.nextInt();
        
        /**
         * 
         * Ahora realizaremos un condicional, para que cuando el segundo
         * sea 0, aparezca un mensaje en pantalla; Y sino es 0
         * haremos la división de ambos números, y mostraremos el resultado
         * en pantalla.
         * 
         */
        
        if (num2 == 0 )
        {
            System.out.println("El segundo número es 0, no se puede dividir");
        }
        else {
            division = (num1/num2);
            System.out.println("El resto de la división es: "+ division);
        }
        
        //Realizamos el resto de operaciones convenientes para el ejercicio
        
        suma = (num1+num2) ;
        resta = (num1-num2) ;
        producto = (num1*num2) ;
        
        //Mostramos en pantalla los resultados de las operaciones hechas.
        
        System.out.println("El resultado de la suma es: "+ suma);
        System.out.println("El resultado de la resta es: "+ resta);
        System.out.println("El reultado de la multiplicación es: "+ producto);
        
        
         
        
    }
    
}
