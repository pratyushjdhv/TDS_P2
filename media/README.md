# Data Analysis Report

### Narrative Analysis of the 'media.csv' Data

#### Overview of the Dataset

The dataset 'media.csv' consists of 2,652 entries, capturing various characteristics of media content over time. The columns represent dates, languages, types of media, titles, creators, and various ratings including overall rating, quality rating, and repeatability scores. This analysis provides insights into overall trends, patterns, and potential anomalies detected in the data.

#### Column-Level Insights

1. **Date**: 
   - The dataset records information spanning different dates, with a notable entry frequency on '21-May-06', which occurs 8 times. 
   - There are 99 missing entries, which indicates potential gaps in data collection during certain timeframes. The scattered nature of the dates could suggest either ongoing data input or unequal media production and release schedules.

2. **Language**:
   - The dataset features content predominantly in English (1,306 entries), with a total of 11 unique languages. This indicates a significant preference or availability of English media.
   - The lack of missing values in this column suggests comprehensive data integrity regarding the language attribute.

3. **Type**:
   - Among the 8 different media types, 'movie' appears dominantly (2,211 entries), suggesting that the dataset primarily captures film content. 
   - This could have implications for understanding audience engagement - it might reflect media consumption trends leaning towards cinematic experiences over other forms.

4. **Title**:
   - The dataset records 2,312 unique titles, with 'Kanda Naal Mudhal' being the most frequently listed at 9 times. The variety in titles indicates a rich catalog of media but could also hint at potential repeated content or franchise flexibility.

5. **By**:
   - Noteworthy is the significant spread of content creators (1,528 unique contributors), with 'Kiefer Sutherland' being the most represented at 48 instances.
   - The existence of 262 missing values in this column suggests a lack of consistent contributor attribution, leading to difficulties in determining overall trends related to specific creators or franchises.

6. **Ratings**:
   - Overall Rating (Mean: 3.05, Std Dev: 0.76): The average rating hovers around the middle, indicating a mix of average to good content. With a max of 5.0 and a min of 1.0, there are opportunities for both highly rated and low-rated media within this dataset.
   - Quality Rating (Mean: 3.21, Std Dev: 0.80): The quality scores are slightly better on average than overall ratings, suggesting that while media may not always resonate well with audiences, it often meets some quality standards.
   - Repeatability Score (Mean: 1.49, Std Dev: 0.60): The repeatability scores lean towards the lower end, with a max of only 3. This signals limited repeated engagement or re-watching of selected media, indicating viewer preferences or simply a broad and diverse selection of new content.

#### Correlation Insights

- The correlation between **overall rating** and **quality rating** (0.83) is notably high, indicating a strong relationship where as quality improves, so too does overall audience satisfaction.
- **Overall rating** and **repeatability** (0.51) show a moderate correlation, which could suggest that more well-rated content is somewhat more likely to be revisited or re-watched.
- Interestingly, **quality rating** and **repeatability** show a lower connection (0.31), which may indicate that high-quality media may not always prompt audiences to rewatch, possibly pointing toward a one-time viewing interest.

#### Trends and Further Analysis

The dataset presents a landscape rich in **media diversity** but predominantly skewed toward films in the English language. Notably, there are gaps in creator data and entry dates that could limit thorough longitudinal analyses of media trends or shifts in audience preferences over time. The high correlation between ratings presents strategic implications for future content production—investing in higher quality may lead to increased overall audience satisfaction and potential repeat engagement.

### Recommendations
To enhance analysis:

- **Data Cleaning**: Impute or handle missing entries, particularly for 'date' and 'by' columns, to improve the robustness of trends derived.
- **Temporal Analysis**: Examine trends over time, especially focusing on release dates to determine if specific periods yield qualitatively better or more popular media.
- **Exploring Audience Engagement**: Further exploration might center on analyzing viewer demographics and viewing behaviors corresponding to content type and ratings, providing deeper insights into how to best engage with audiences going forward. 

Overall, 'media.csv' delivers a foundational insight into media consumption patterns, which, with further inquiry, could lead to more strategic content development and distribution decisions.

## Visualizations

![correlation_heatmap.png](correlation_heatmap.png)
![overall_distribution.png](overall_distribution.png)
![pairplot.png](pairplot.png)
![quality_distribution.png](quality_distribution.png)
![repeatability_distribution.png](repeatability_distribution.png)
![type_countplot.png](type_countplot.png)