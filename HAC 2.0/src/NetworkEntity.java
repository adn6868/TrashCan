import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketException;
import java.net.UnknownHostException;
public class NetworkEntity {
	public DatagramSocket socket;
	public String name;
	
	static int staticId;
	
	private byte[] buf;
	private DatagramPacket packet;
	private InetAddress ip;
	private int id;
	
	public NetworkEntity() 
	{
		buf = new byte[1024];
		id = staticId;
		name = String.format("Network Entity %d", staticId);
		packet = new DatagramPacket(buf, buf.length);
		staticId ++;
		try 
		{
			socket = new DatagramSocket(1412);
			this.ip = InetAddress.getLocalHost();
		} catch (UnknownHostException|SocketException  e) 
		{
			System.err.print(e);
		}
	}
	public String toString() {
		return String.format("ID: %s, Name %s, buf size %d, packet: %s", this.id,this.name,
				this.buf.length,this.packet.toString());
	}
	public void setBuffer (byte[] buf) {
		this.buf = buf;
	}
	public int getID() 
	{
		return this.id;
	}
	public String getName() 
	{
		return this.name;
	}
	public InetAddress getIP() 
	{
		return this.ip;
	}
	public void setName(String name) 
	{
		this.name = name;
	}
	
	//	byte[] buf = new byte[1024];
//	DatagramPacket packet = new DatagramPacket(buf, buf.length);
//	InetAddress ip = packet
}
