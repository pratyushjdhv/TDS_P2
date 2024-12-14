# Data Analysis Report

The data analysis of 'media.csv' reveals several interesting trends and patterns within the dataset pertaining to media entries, likely reviews or ratings of various media types. Here’s a comprehensive narrative based on the findings:

### Data Overview
The dataset comprises 2,652 entries, representing various media items characterized by attributes such as date of entry, language, type, title, contributor (by), overall rating, quality rating, and repeatability rating. Notably, the date field has 99 missing values, indicating that it is less complete compared to other fields, particularly the 'by' field, which has 262 missing entries.

### Language and Type Distribution
Upon examining the 'language' column, English emerges as the dominant language, accounting for 1,306 entries. The dataset showcases a variety of 11 different languages, indicating a diverse range of media offerings. Additionally, the predominant type of media is movies, with 2,211 recorded instances, illustrating a strong inclination towards film-related content over other types.

### Title Popularity
The title analysis indicates that "Kanda Naal Mudhal" is the most frequent title, appearing nine times in the dataset. With a unique title count of 2,312, this suggests a rich variety of media available for review. However, the occurrence of repeated titles could suggest either a trend in popular media or perhaps variations like different reviews for the same title.

### Contributor Insights
In terms of individual contributions, Kiefer Sutherland is noted as the most frequently credited individual with 48 entries. This might require further exploration into whether his contributions are consistent in context or vary widely between different media types. The total unique contributors count stands at 1,528, indicating a significant number of reviewers providing diverse opinions.

### Ratings Overview
The performance metrics provided—overall, quality, and repeatability ratings—underscore a moderately favorable perception of the media. The average overall rating is approximately 3.05 out of 5, with a standard deviation of 0.76, suggesting that, while opinions are generally positive, there is variability in satisfaction levels. The quality metric averages at 3.21 with a standard deviation of 0.80, further reinforcing a trend of positive yet varied experiences among users.

The repeatability rating, averaging at 1.49, indicates that most reviewers do not expect to re-engage with the media, which might suggest that once is generally sufficient for satisfaction—either because of the content's nature or user preference.

### Correlation Insights
The correlation matrix shows significant relationships between the ratings. The correlation of 0.83 between overall and quality ratings indicates a strong positive relationship: as perceived quality increases, so does the overall rating. The repeatability rating, while lower correlated at 0.51 with overall, indicates a moderate association, suggesting that those who rate media highly do perhaps reflect a tendency towards repeat engagement, albeit not as strongly.

### Missing Value Consideration
The presence of missing values, especially in the date and contributor fields, indicates the need for improved data collection practices. Missing dates could obscure temporal trends in media reviews, such as shifts in user preferences over time, while missing contributor data might limit insights into the diversity and credibility of reviews.

### Trends and Patterns
1. **Cultural Influence**: The predominance of English media and films indicates possible cultural biases, potentially underrepresenting non-English media types.
   
2. **User Engagement**: The repeatability score suggests that while users may enjoy certain media, the necessity to engage with them again is minimal, indicating a one-time experience satisfaction.

3. **Quality Implication**: Higher scores in quality directly elevate the overall perception of the media, highlighting the importance of content quality in user satisfaction.

### Conclusion
Overall, the analysis paints a picture of a diverse media dataset with robust user engagement and commentary. While predominantly focused on movies in English, the emerging metrics reveal general positive sentiments towards media quality and user satisfaction, though with variability present. Additionally, attention to missing data fields will be beneficial for future analyses to better understand trends over time and among different contributor demographics.

## Visualizations

![correlation_heatmap.png](correlation_heatmap.png)
![overall_distribution.png](overall_distribution.png)
![pairplot.png](pairplot.png)
![quality_distribution.png](quality_distribution.png)
![repeatability_distribution.png](repeatability_distribution.png)
![type_countplot.png](type_countplot.png)