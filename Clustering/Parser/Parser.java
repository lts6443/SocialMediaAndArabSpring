import java.io.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.regex.*;

import org.json.*;

/**
 * Parses json tweet data into a binary matrix csv of hashags
 * reads in data from tweets.json
 * writes to a new file called sampledata.csv
 * 
 * @author Lou, Joe, Vino
 */

public class IntelSecuritySystems {

	private static final String FILENAME = "tweets.json";
	// Regex to find hashtags
	private static final Pattern HASHTAG_PATTERN = Pattern.compile("(|\"|^|\\?)#[A-Za-z0-9]*(|\"|$|\\?|')");
	
	public static void main(String[] args) {
		// Hashmap stores
		HashMap<String, ArrayList<Integer>> hashtagMap = new HashMap<String, ArrayList<Integer>>();
		
		BufferedReader br;
		String line = "";
		int index = 0;
		try {
			br = new BufferedReader(new FileReader(FILENAME));
			//loop through all lines
			while ((line = br.readLine()) != null) {
				// Adds a new index to all arrays in the hashmap
				for (String hashtag: hashtagMap.keySet()) {
					hashtagMap.get(hashtag).add(0);
				}
				
				ArrayList<String> hash = new ArrayList<String>();
				// Extracts Json
				JSONObject obj = new JSONObject(line);
				String text = obj.getString("text");
				
				// Split the line on whitespace
				String[] tokens = text.split("\\s");
				for (String s: tokens) {
					Matcher m = HASHTAG_PATTERN.matcher(s);
					
					while (m.find()) {
					    String hashtag = m.group(0).toLowerCase();
					    if (hashtagMap.containsKey(hashtag)) {
					    	hashtagMap.get(hashtag).add(index, 1);
					    } else {
					    	ArrayList<Integer> newList = new ArrayList<Integer>();
					    	for (int i = 0; i < index; i++) {
					    		newList.add(0);
					    	}
					    	newList.add(1);
					    	hashtagMap.put(hashtag, newList);
					    }
					}
				}
				index++;
			}
			br.close();
			
	 
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		PrintWriter writer;
		
		// Ouput the CSV to the new file sampledata.txt
		try {
			writer = new PrintWriter("sampledata.csv", "UTF-8");
			int j = 0;
			for (String hashtag: hashtagMap.keySet()) {
				writer.print(j++ + hashtag+",");
			}
			writer.println("");
			for (int i = 0; i < index; i++) {
				for (String hashtag: hashtagMap.keySet()) {
					writer.print(hashtagMap.get(hashtag).get(i) + ",");
				}
				writer.println("");
			}
			
			writer.close();
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (UnsupportedEncodingException e) {
			e.printStackTrace();
		}
	}
}
