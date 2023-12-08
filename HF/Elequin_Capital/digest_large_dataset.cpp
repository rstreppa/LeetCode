#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <numeric>
#include <nlohmann/json.hpp>

using json = nlohmann::json;
using namespace std;

class FineArtMarketAnalyzer {
private:
    struct ArtSale {
        string work_uid;
        string purchaser_name;
        long long purchase_timestamp;
        double purchase_price_usd;
    };

    vector<ArtSale> data;

public:
    FineArtMarketAnalyzer(const string& file_path) {
        this->load_and_clean_data(file_path);
    }

    /* 
        The load_and_clean_data method reads the file character by character, similar to the Python version, and uses a simple state machine to manage skipping the appearance_at_purchase data.
    */
    void load_and_clean_data(const string& file_path) {
        ifstream file(file_path);
        string buffer;
        char ch;
        bool skip = false;
        bool inObject = false;

        while (file.get(ch)) {
            if (ch == '{') {
                skip = false;
                inObject = true;
                buffer.clear();
                buffer += ch;
            } else if (ch == '}' && inObject) {
                buffer += ch;
                if (!skip) {
                    // Parse the JSON object and add it to the data vector
                    json art_json = json::parse(buffer);
                    ArtSale sale;
                    sale.work_uid = art_json["work_uid"];
                    sale.purchaser_name = art_json["purchaser_name"];
                    sale.purchase_timestamp = art_json["purchase_timestamp"];
                    sale.purchase_price_usd = art_json["purchase_price_usd"];
                    data.push_back(sale);
                }
                inObject = false;
            } else if (inObject) {
                if (!skip) buffer += ch;
                if (buffer.find("\"appearance_at_purchase\":") != string::npos) {
                    skip = true;
                    buffer.erase(buffer.find("\"appearance_at_purchase\":"));
                }
            }
        }
    }
    double median_sale_price() {
        vector<double> prices;
        for (const auto& sale : data) {
            prices.push_back(sale.purchase_price_usd);
        }
        sort(prices.begin(), prices.end());
        int n = prices.size();
        return n % 2 == 0 ? (prices[n / 2 - 1] + prices[n / 2]) / 2 : prices[n / 2];
    }

    void calculate_z_scores(vector<double>& z_scores) {
        double mean = accumulate(data.begin(), data.end(), 0.0, 
            [](double sum, const ArtSale& sale) { return sum + sale.purchase_price_usd; }) / data.size();

        double variance = accumulate(data.begin(), data.end(), 0.0, 
            [mean](double sum, const ArtSale& sale) {
                return sum + (sale.purchase_price_usd - mean) * (sale.purchase_price_usd - mean);
            }) / data.size();

        double std_dev = sqrt(variance);

        for (const auto& sale : data) {
            z_scores.push_back((sale.purchase_price_usd - mean) / std_dev);
        }
    }

    pair<double, double> ols_regression_analysis() {
        double x_mean = accumulate(data.begin(), data.end(), 0.0, 
            [](double sum, const ArtSale& sale) { return sum + sale.purchase_timestamp; }) / data.size();
        
        double y_mean = accumulate(data.begin(), data.end(), 0.0, 
            [](double sum, const ArtSale& sale) { return sum + sale.purchase_price_usd; }) / data.size();

        double numerator = 0.0;
        double denominator = 0.0;
        for (const auto& sale : data) {
            numerator += (sale.purchase_timestamp - x_mean) * (sale.purchase_price_usd - y_mean);
            denominator += (sale.purchase_timestamp - x_mean) * (sale.purchase_timestamp - x_mean);
        }

        double slope = numerator / denominator;
        double intercept = y_mean - slope * x_mean;

        double total_var = 0.0;
        double explained_var = 0.0;
        for (const auto& sale : data) {
            double y_pred = slope * sale.purchase_timestamp + intercept;
            total_var += (sale.purchase_price_usd - y_mean) * (sale.purchase_price_usd - y_mean);
            explained_var += (y_pred - y_mean) * (y_pred - y_mean);
        }

        double r_squared = explained_var / total_var;
        return {slope, r_squared};
    }

    map<string, double> total_spends_per_purchaser() {
        map<string, double> spends;
        for (const auto& sale : data) {
            spends[sale.purchaser_name] += sale.purchase_price_usd;
        }
        return spends;
    }

    string most_frequently_traded_work() {
        map<string, int> trade_counts;
        for (const auto& sale : data) {
            trade_counts[sale.work_uid]++;
        }

        return max_element(trade_counts.begin(), trade_counts.end(),
            [](const pair<string, int>& a, const pair<string, int>& b) {
                return a.second < b.second;
            })->first;
    }
};

int main() {
    FineArtMarketAnalyzer analyzer("path_to_file.json");
    double median_price = analyzer.median_sale
