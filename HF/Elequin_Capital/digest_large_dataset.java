import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class FineArtMarketAnalyzer {
    private static class ArtSale {
        String workUid;
        String purchaserName;
        long purchaseTimestamp;
        double purchasePriceUsd;
    }

    private List<ArtSale> data = new ArrayList<>();

    public FineArtMarketAnalyzer(String filePath) throws IOException {
        this.loadAndCleanData(filePath);
    }

    private void loadAndCleanData(String filePath) throws IOException {
        File file = new File(filePath);
        BufferedReader reader = new BufferedReader(new FileReader(file));
        StringBuilder buffer = new StringBuilder();
        int ch;
        boolean skip = false;
        boolean inObject = false;

        while ((ch = reader.read()) != -1) {
            char charCh = (char) ch;
            if (charCh == '{') {
                skip = false;
                inObject = true;
                buffer = new StringBuilder();
                buffer.append(charCh);
            } else if (charCh == '}' && inObject) {
                buffer.append(charCh);
                if (!skip) {
                    // Parse the JSON object and add it to the data list
                    ObjectMapper mapper = new ObjectMapper();
                    JsonNode artJson = mapper.readTree(buffer.toString());
                    ArtSale sale = new ArtSale();
                    sale.workUid = artJson.get("work_uid").asText();
                    sale.purchaserName = artJson.get("purchaser_name").asText();
                    sale.purchaseTimestamp = artJson.get("purchase_timestamp").asLong();
                    sale.purchasePriceUsd = artJson.get("purchase_price_usd").asDouble();
                    data.add(sale);
                }
                inObject = false;
            } else if (inObject) {
                if (!skip) buffer.append(charCh);
                if (buffer.toString().contains("\"appearance_at_purchase\":")) {
                    skip = true;
                    int index = buffer.toString().indexOf("\"appearance_at_purchase\":");
                    buffer = new StringBuilder(buffer.substring(0, index));
                }
            }
        }
        reader.close();
    }

    public double medianSalePrice() {
        List<Double> prices = data.stream().map(sale -> sale.purchasePriceUsd).sorted().collect(Collectors.toList());
        int n = prices.size();
        return n % 2 == 0 ? (prices.get(n / 2 - 1) + prices.get(n / 2)) / 2 : prices.get(n / 2);
    }

    public List<Double> calculateZScores() {
        double mean = data.stream().mapToDouble(sale -> sale.purchasePriceUsd).average().orElse(0.0);
        double variance = data.stream().mapToDouble(sale -> (sale.purchasePriceUsd - mean) * (sale.purchasePriceUsd - mean)).average().orElse(0.0);
        double stdDev = Math.sqrt(variance);

        return data.stream().map(sale -> (sale.purchasePriceUsd - mean) / stdDev).collect(Collectors.toList());
    }

    public Map.Entry<Double, Double> olsRegressionAnalysis() {
        double xMean = data.stream().mapToDouble(sale -> sale.purchaseTimestamp).average().orElse(0.0);
        double yMean = data.stream().mapToDouble(sale -> sale.purchasePriceUsd).average().orElse(0.0);

        double numerator = data.stream().mapToDouble(sale -> (sale.purchaseTimestamp - xMean) * (sale.purchasePriceUsd - yMean)).sum();
        double denominator = data.stream().mapToDouble(sale -> (sale.purchaseTimestamp - xMean) * (sale.purchaseTimestamp - xMean)).sum();

        double slope = numerator / denominator;
        double intercept = yMean - slope * xMean;

        double totalVar = data.stream().mapToDouble(sale -> (sale.purchasePriceUsd - yMean) * (sale.purchasePriceUsd - yMean)).sum();
        double explainedVar = data.stream().mapToDouble(sale -> {
            double yPred = slope * sale.purchaseTimestamp + intercept;
            return (yPred - yMean) * (yPred - yMean);
        }).sum();

        double rSquared = explainedVar / totalVar;
        return new AbstractMap.SimpleEntry<>(slope, rSquared);
    }

    public Map<String, Double> totalSpendsPerPurchaser() {
        Map<String, Double> spends = new HashMap<>();
        for (ArtSale sale : data)
