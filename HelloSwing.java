import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class HelloSwing {
    public static void main(String[] args) {

        JFrame frame = new JFrame("Dialog Box!");
        frame.setSize(400, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);


        JPanel panel = new JPanel();


        JButton button = new JButton("Click Me");



        button.addActionListener(new ActionListener() {

            public void actionPerformed(ActionEvent e) {

                JOptionPane.showMessageDialog(frame, "Hello, Swing!");
            }
        });


        panel.add(button);


        frame.getContentPane().add(panel, BorderLayout.CENTER);


        frame.setLocationRelativeTo(null);


        frame.setVisible(true);
    }
}
