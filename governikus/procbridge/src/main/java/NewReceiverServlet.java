import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.xml.transform.TransformerException;
import javax.xml.transform.TransformerFactoryConfigurationError;
import java.io.IOException;
import co.gongzh.procbridge.ProcBridge;
import co.gongzh.procbridge.ProcBridgeException;
import org.json.JSONObject;
import com.google.gson.Gson;


public class NewReceiverServlet extends HttpServlet {
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException,
            IOException {
        String host = "demo";
        int port = 8877;
        long timeout = 10000; // 10 seconds

        PersonalData pd = new PersonalData();

        ProcBridge pb = new ProcBridge(host, port, timeout);
        Gson gson = new Gson();

        try {
            //JSONObject resp;
            String args = gson.toJson(pd);
            System.out.println("Args: " + args);


            JSONObject resp = pb.request("storeNPAData", args);
            System.out.println(resp);

        } catch (ProcBridgeException e) {
            e.printStackTrace();
        }
    }
}
