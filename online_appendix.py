import os
import pandas as pd
import numpy as np
current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)


indices = ["AEX", "AORD", "BFX", "BSESN", "BVSP", "DJI", "FCHI", "FTSE", "GDAXI", "HSI", 
           "IBEX", "IXIC", "KS11", "KSE", "MXX", "N225", "NSEI", "RUT", "SPX", "SSEC", "SSMI", "S5E"]
pairs = [
    "AEX/AORD", "AEX/BFX", "AEX/BSESN", "AEX/BVSP", "AEX/DJI", "AEX/FCHI", "AEX/FTSE", 
    "AEX/GDAXI", "AEX/HSI", "AEX/IBEX", "AEX/IXIC", "AEX/KS11", "AEX/KSE", "AEX/MXX", 
    "AEX/N225", "AEX/NSEI", "AEX/RUT", "AEX/SPX", "AEX/SSEC", "AEX/SSMI", "AEX/S5E", 
    "AORD/BFX", "AORD/BSESN", "AORD/BVSP", "AORD/DJI", "AORD/FCHI", "AORD/FTSE", "AORD/GDAXI", 
    "AORD/HSI", "AORD/IBEX", "AORD/IXIC", "AORD/KS11", "AORD/KSE", "AORD/MXX", "AORD/N225", 
    "AORD/NSEI", "AORD/RUT", "AORD/SPX", "AORD/SSEC", "AORD/SSMI", "AORD/S5E", "BFX/BSESN", 
    "BFX/BVSP", "BFX/DJI", "BFX/FCHI", "BFX/FTSE", "BFX/GDAXI", "BFX/HSI", "BFX/IBEX", 
    "BFX/IXIC", "BFX/KS11", "BFX/KSE", "BFX/MXX", "BFX/N225", "BFX/NSEI", "BFX/RUT", 
    "BFX/SPX", "BFX/SSEC", "BFX/SSMI", "BFX/S5E", "BSESN/BVSP", "BSESN/DJI", "BSESN/FCHI", 
    "BSESN/FTSE", "BSESN/GDAXI", "BSESN/HSI", "BSESN/IBEX", "BSESN/IXIC", "BSESN/KS11", 
    "BSESN/KSE", "BSESN/MXX", "BSESN/N225", "BSESN/NSEI", "BSESN/RUT", "BSESN/SPX", 
    "BSESN/SSEC", "BSESN/SSMI", "BSESN/S5E", "BVSP/DJI", "BVSP/FCHI", "BVSP/FTSE", 
    "BVSP/GDAXI", "BVSP/HSI", "BVSP/IBEX", "BVSP/IXIC", "BVSP/KS11", "BVSP/KSE", "BVSP/MXX", 
    "BVSP/N225", "BVSP/NSEI", "BVSP/RUT", "BVSP/SPX", "BVSP/SSEC", "BVSP/SSMI", "BVSP/S5E", 
    "DJI/FCHI", "DJI/FTSE", "DJI/GDAXI", "DJI/HSI", "DJI/IBEX", "DJI/IXIC", "DJI/KS11", 
    "DJI/KSE", "DJI/MXX", "DJI/N225", "DJI/NSEI", "DJI/RUT", "DJI/SPX", "DJI/SSEC", 
    "DJI/SSMI", "DJI/S5E", "FCHI/FTSE", "FCHI/GDAXI", "FCHI/HSI", "FCHI/IBEX", "FCHI/IXIC", 
    "FCHI/KS11", "FCHI/KSE", "FCHI/MXX", "FCHI/N225", "FCHI/NSEI", "FCHI/RUT", "FCHI/SPX", 
    "FCHI/SSEC", "FCHI/SSMI", "FCHI/S5E", "FTSE/GDAXI", "FTSE/HSI", "FTSE/IBEX", 
    "FTSE/IXIC", "FTSE/KS11", "FTSE/KSE", "FTSE/MXX", "FTSE/N225", "FTSE/NSEI", "FTSE/RUT", 
    "FTSE/SPX", "FTSE/SSEC", "FTSE/SSMI", "FTSE/S5E", "GDAXI/HSI", "GDAXI/IBEX", 
    "GDAXI/IXIC", "GDAXI/KS11", "GDAXI/KSE", "GDAXI/MXX", "GDAXI/N225", "GDAXI/NSEI", 
    "GDAXI/RUT", "GDAXI/SPX", "GDAXI/SSEC", "GDAXI/SSMI", "GDAXI/S5E", "HSI/IBEX", 
    "HSI/IXIC", "HSI/KS11", "HSI/KSE", "HSI/MXX", "HSI/N225", "HSI/NSEI", "HSI/RUT", 
    "HSI/SPX", "HSI/SSEC", "HSI/SSMI", "HSI/S5E", "IBEX/IXIC", "IBEX/KS11", "IBEX/KSE", 
    "IBEX/MXX", "IBEX/N225", "IBEX/NSEI", "IBEX/RUT", "IBEX/SPX", "IBEX/SSEC", "IBEX/SSMI", 
    "IBEX/S5E", "IXIC/KS11", "IXIC/KSE", "IXIC/MXX", "IXIC/N225", "IXIC/NSEI", "IXIC/RUT", 
    "IXIC/SPX", "IXIC/SSEC", "IXIC/SSMI", "IXIC/S5E", "KS11/KSE", "KS11/MXX", "KS11/N225", 
    "KS11/NSEI", "KS11/RUT", "KS11/SPX", "KS11/SSEC", "KS11/SSMI", "KS11/S5E", "KSE/MXX", 
    "KSE/N225", "KSE/NSEI", "KSE/RUT", "KSE/SPX", "KSE/SSEC", "KSE/SSMI", "KSE/S5E", 
    "MXX/N225", "MXX/NSEI", "MXX/RUT", "MXX/SPX", "MXX/SSEC", "MXX/SSMI", "MXX/S5E", 
    "N225/NSEI", "N225/RUT", "N225/SPX", "N225/SSEC", "N225/SSMI", "N225/S5E", 
    "NSEI/RUT", "NSEI/SPX", "NSEI/SSEC", "NSEI/SSMI", "NSEI/S5E", "RUT/SPX", "RUT/SSEC", 
    "RUT/SSMI", "RUT/S5E", "SPX/SSEC", "SPX/SSMI", "SPX/S5E", "SSEC/SSMI", 
    "SSEC/S5E", "SSMI/S5E"
]

# List to store HTML filenames for the five pages
pages = ['page0_ind.html', 'page1_ccfe.html', 'page2_ccfl.html', 'page3_esta.html', 'page4_ccfa.html', 'page5_estc.html', 'page6_ccfc.html']
html_content_page = ["", "", "", "", "", "", ""]
# %% 0: Index
html_content_page[0] += """
<!DOCTYPE html>
<html>
    <style>
    body {
           font-size: 18px; /* Adjust the base font size */
           font-family: Arial, sans-serif; /* Optional: Change font family */
       }
    </style>
    
<!-- Index -->
<div>
    <h2>Online Appendix (Dugo Giorgio Pigato 2024b)</h2>
    <p> This document serves as a supplementary appendix to the paper "Multivariate Rough Volatility" (Dugo, Giorgio, Pigato 2024b), which is available at <a href="https://arxiv.org/pdf/2412.14353" target="_blank">
          https://arxiv.org/pdf/2412.14353
        </a>. Readers are encouraged to consult the main paper, as the content in this appendix is not self-explanatory. </p>
    <h2>Navigation Index</h2>
    <ul>
        <li><a href="page1_ccfe.html">1. Goodness of covariance fit (exact estimation)</a></li>
        contains additional evidence of the goodness of fit of our model to the data by showing empirical and theoretical cross-covariances with estimates according to Section 5.1. </p> 
        <li><a href="page2_ccfl.html">2. Empirical evidence of asymptotic regime</a></li>
        contains plots of the auto and cross-covariances as functions of suitable powers of the lags, which, according to the asymptotic relationship, should be linear.</p>  
        <li><a href="page3_esta.html">3. Estimates in the asymptotic regime</a></li>
        presents estimates of the model in the small alpha regime, where we employ asymptotic auto and cross-covariances as conditions in the estimation procedure.</p>
        <li><a href="page4_ccfa.html">4. Goodness of covariance fit (asymptotic regime)</a></li>
        contains additional evidence of the goodness of fit of our model in the asymptotic regime to the data by showing empirical and theoretical cross-covariances with estimates in line with Section 5.2. </p> 
        <li><a href="page5_estc.html">5. Estimates in the causal regime</a></li>
        contains estimates of the model in the causal regime, where eta is constrained to be a function of rho, H1 and H2. </p> 
        <li><a href="page6_ccfc.html">6. Goodness of covariance fit (causal regime)</a></li>
        contains evidence of the goodness of fit of our model in the causal regime (used in the spillover analysis) to the data by showing empirical and theoretical cross-covariances. </p> 
    </ul>
</div>
"""

# %% 1: Goodness of fit exact
html_content_page[1] += """
<!DOCTYPE html>
<html>

<head>
    <style>
    body {
           font-size: 18px; /* Adjust the base font size */
           font-family: Arial, sans-serif; /* Optional: Change font family */
       }
        .search-box { margin: 20px; }
        select { width: 250px; padding: 10px; font-size: 16px; }
        option { font-size: 18px; }
        .dropdown { margin-bottom: 20px; }
    </style>
</head>
<body>

<h1>Goodness of covariance fit (exact conditions)</h1>
<p> The following plots display the empirical auto and cross-covariances (represented by bars) of realized volatilities from the Oxford-Man dataset, alongside the mfOU-implied theoretical ones (depicted by red curves). The theoretical auto and cross-covariances are calculated using parameters obtained through minimum distance estimation (MDE), which targets the distance between empirical and theoretical quantities shown in the plots. For more details, please refer to Section 5.1. </p>

<!-- Index Dropdown -->
<div class="dropdown">
    <label for="indexDropdown">Autocovariance:</label>
    <select id="indexDropdown" onchange="scrollToPlot('index')">
        <option value="">Select an index</option>
"""

# Adding options for indices dropdown
for s1 in indices:
    html_content_page[1] += f'<option value="{s1}">{s1}</option>'

html_content_page[1] += "</select></div>"

# Pairs Dropdown
html_content_page[1] += """
<div class="dropdown">
    <label for="pairDropdown">Cross-covariance:</label>
    <select id="pairDropdown" onchange="scrollToPlot('pair')">
        <option value="">Select a pair</option>
"""

# Adding options for pairs dropdown
for pair in pairs:
    s1, s2 = pair.split('/')
    s12 = s1 + "_" + s2  # This creates a unique ID like 'AEX_AORD' for 'AEX/AORD'
    html_content_page[1] += f'<option value="{s12}">{pair}</option>'

html_content_page[1] += "</select></div>"

# Add plots for each index and pair
for s1 in indices:    
    html_content_page[1] += f"""
    <div id="{s1}" style="width:1000px; display: flex; justify-content: space-between; gap: 0px; margin: 0; padding: 0;">
        <figure class="left" style="margin-right: -3px;">
            <img src="files_online_appendix/acfe_{s1}.png" width="500" height="500"/>
        </figure>
    </div>
    """

for pair in pairs:
    s1, s2 = pair.split('/')
    s12 = s1 + "_" + s2  # Unique ID like 'AEX_AORD' for 'AEX/AORD'
    
    html_content_page[1] += f"""
    <div id="{s12}" style="width:1000px; display: flex; justify-content: space-between; gap: 0px; margin: -20px 0 0 0; padding: 0;">
        <figure class="left" style="float:left">
            <img src="files_online_appendix/ccfe_{s12}.png" width="1000" height="500"/>
        </figure>
    </div>
    """

# JavaScript for scrolling to selected plots
html_content_page[1] += """
<script>
    function scrollToPlot(type) {
        let dropdown = document.getElementById(type === 'index' ? 'indexDropdown' : 'pairDropdown');
        let value = dropdown.value;
        if (value) {
            let plot = document.getElementById(value);
            plot.scrollIntoView({ behavior: 'smooth' });
        }
    }
</script>

</body>
</html>
"""


# %% 2: Goodness of fit linear
html_content_page[2] += """
<!DOCTYPE html>
<html>

<head>
    <style>
    body {
           font-size: 18px; /* Adjust the base font size */
           font-family: Arial, sans-serif; /* Optional: Change font family */
       }
        .search-box { margin: 20px; }
        select { width: 250px; padding: 10px; font-size: 16px; }
        option { font-size: 16px; }
        .dropdown { margin-bottom: 20px; }
    </style>
</head>
<body>

<h1>Empirical evidence of asymptotic regime</h1>
<p> The following plots display the empirical auto and cross-covariances of realized volatilities from the Oxford-Man library, represented as bars, plotted against appropriate powers of the lags. These lags are determined based on the pre-estimated Hurst exponents. The best linear fits are shown in red. This provides an empirical validation of the linearity predicted by the small-alpha (equivalently, small-k) asymptotic relationship. This is also referred to as slow mean reversion in the main paper. Best linear fits are consistently below the actual value of the variance (autocovariance at lag 0). The residual part at lag 0 might be attributable to the measurement error of integrated variance, if assumed to have the same structure as in Bolko et. al (2023).</p>

<!-- Index Dropdown -->
<div class="dropdown">
    <label for="indexDropdown">Autocovariance:</label>
    <select id="indexDropdown" onchange="scrollToPlot('index')">
        <option value="">Select an index</option>
"""

# Adding options for indices dropdown
for s1 in indices:
    html_content_page[2] += f'<option value="{s1}">{s1}</option>'

html_content_page[2] += "</select></div>"

# Pairs Dropdown
html_content_page[2] += """
<div class="dropdown">
    <label for="pairDropdown">Cross-covariance:</label>
    <select id="pairDropdown" onchange="scrollToPlot('pair')">
        <option value="">Select a pair</option>
"""

# Adding options for pairs dropdown
for pair in pairs:
    s1, s2 = pair.split('/')
    s12 = s1 + "_" + s2  # This creates a unique ID like 'AEX_AORD' for 'AEX/AORD'
    html_content_page[2] += f'<option value="{s12}">{pair}</option>'

html_content_page[2] += "</select></div>"

# Add plots for each index and pair
for s1 in indices:    
    html_content_page[2] += f"""
    <div id="{s1}" style="width:1000px; display: flex; justify-content: space-between; gap: 0px; margin: 0; padding: 0;">
        <figure class="left" style="margin-right: -3px;">
            <img src="files_online_appendix/acfl_{s1}.png" width="500" height="500"/>
        </figure>
    </div>
    """

for pair in pairs:
    s1, s2 = pair.split('/')
    s12 = s1 + "_" + s2  # Unique ID like 'AEX_AORD' for 'AEX/AORD'
    
    html_content_page[2] += f"""
    <div id="{s12}" style="width:1000px; display: flex; justify-content: space-between; gap: 0px; margin: -20px 0 0 0; padding: 0;">
        <figure class="left" style="float:left">
            <img src="files_online_appendix/ccfl_{s12}.png" width="1000" height="500"/>
        </figure>
    </div>
    """

# JavaScript for scrolling to selected plots
html_content_page[2] += """
<script>
    function scrollToPlot(type) {
        let dropdown = document.getElementById(type === 'index' ? 'indexDropdown' : 'pairDropdown');
        let value = dropdown.value;
        if (value) {
            let plot = document.getElementById(value);
            plot.scrollIntoView({ behavior: 'smooth' });
        }
    }
</script>

</body>
</html>
"""

# %% 3: Estimates Asym
html_content_page[3] += """
<style>
body {
       font-size: 18px; /* Adjust the base font size */
       font-family: Arial, sans-serif; /* Optional: Change font family */
   }
</style>

<h1>Estimates in the asymptotic regime</h1>
<p> The following tables present empirical parameter estimates for the model (mfOU) in the small-alpha regime, where it is assumed that the cross-covariance function follows the asymptotic relationship. The asymptotic cross-covariance relationship is directly incorporated into the minimum distance estimation (MDE). For more details, please refer to Section 5.2, where this regime is referred to as slow mean reversion. </p>
"""
tUniv4 = pd.read_csv("files_online_appendix/table_asy_univ.csv").round(3)
mRho4 = pd.read_csv("files_online_appendix/matrix_asy_rho.csv").round(3)
mEta4 = pd.read_csv("files_online_appendix/matrix_asy_eta.csv").round(3)
mCov4 = pd.read_csv("files_online_appendix/matrix_asy_cov.csv").round(3)
mRho4.index = mRho4.columns
mEta4.index = mEta4.columns
mCov4.index = mCov4.columns

for i in range(len(mRho4.columns)):
    mRho4.iloc[:i, i] = np.nan
    mEta4.iloc[:i, i] = np.nan
    mCov4.iloc[:i, i] = np.nan

html_content_page[3] +="""
<h2>Univariate estimates</h2>
"""
html_content_page[3] += tUniv4.to_html(index=False, na_rep='')
html_content_page[3] +="""
<br>
<br>
<h2>Matrix RHO</h2>
"""
html_content_page[3] += mRho4.to_html(index=True, na_rep='')
html_content_page[3] +="""
<br>
<br>
<h2>Matrix ETA</h2>
"""
html_content_page[3] += mEta4.to_html(index=True, na_rep='')
html_content_page[3] +="""
<br>
<br>
<h2>Matrix COV</h2>
"""
html_content_page[3] += mCov4.to_html(index=True, na_rep='')
# %% 4: Goodness of fit Asym
html_content_page[4] += """
<!DOCTYPE html>
<html>

<head>
    <style>
    body {
           font-size: 18px; /* Adjust the base font size */
           font-family: Arial, sans-serif; /* Optional: Change font family */
       }
        .search-box { margin: 20px; }
        select { width: 250px; padding: 10px; font-size: 16px; }
        option { font-size: 16px; }
        .dropdown { margin-bottom: 20px; }
    </style>
</head>
<body>

<h1>Goodness of covariance fit (asymptotic regime)</h1>
<p> The following plots display the empirical auto and cross-covariances (represented by bars) of realized volatilities from the Oxford-Man dataset, alongside the mfOU-implied small-alpha theoretical ones (depicted by red curves). The (asymptotic) theoretical auto and cross-covariances are calculated using parameters obtained through minimum distance estimation (MDE), which targets the distance between empirical and theoretical quantities shown in the plots. For more details, please refer to Section 5.2, where this regime is referred to as slow mean reversion. </p>

<!-- Index Dropdown -->
<div class="dropdown">
    <label for="indexDropdown">Autocovariance:</label>
    <select id="indexDropdown" onchange="scrollToPlot('index')">
        <option value="">Select an index</option>
"""

# Adding options for indices dropdown
for s1 in indices:
    html_content_page[4] += f'<option value="{s1}">{s1}</option>'

html_content_page[4] += "</select></div>"

# Pairs Dropdown
html_content_page[4] += """
<div class="dropdown">
    <label for="pairDropdown">Cross-covariance:</label>
    <select id="pairDropdown" onchange="scrollToPlot('pair')">
        <option value="">Select a pair</option>
"""

# Adding options for pairs dropdown
for pair in pairs:
    s1, s2 = pair.split('/')
    s12 = s1 + "_" + s2  # This creates a unique ID like 'AEX_AORD' for 'AEX/AORD'
    html_content_page[4] += f'<option value="{s12}">{pair}</option>'

html_content_page[4] += "</select></div>"

# Add plots for each index and pair
for s1 in indices:    
    html_content_page[4] += f"""
    <div id="{s1}" style="width:1000px; display: flex; justify-content: space-between; gap: 0px; margin: 0; padding: 0;">
        <figure class="left" style="margin-right: -3px;">
            <img src="files_online_appendix/acfa_{s1}.png" width="500" height="500"/>
        </figure>
    </div>
    """

for pair in pairs:
    s1, s2 = pair.split('/')
    s12 = s1 + "_" + s2  # Unique ID like 'AEX_AORD' for 'AEX/AORD'
    
    html_content_page[4] += f"""
    <div id="{s12}" style="width:1000px; display: flex; justify-content: space-between; gap: 0px; margin: -20px 0 0 0; padding: 0;">
        <figure class="left" style="float:left">
            <img src="files_online_appendix/ccfa_{s12}.png" width="1000" height="500"/>
        </figure>
    </div>
    """

# JavaScript for scrolling to selected plots
html_content_page[4] += """
<script>
    function scrollToPlot(type) {
        let dropdown = document.getElementById(type === 'index' ? 'indexDropdown' : 'pairDropdown');
        let value = dropdown.value;
        if (value) {
            let plot = document.getElementById(value);
            plot.scrollIntoView({ behavior: 'smooth' });
        }
    }
</script>

</body>
</html>
"""

# %% 5: Estimates Causal
html_content_page[5] +="""
<style>
body {
       font-size: 18px; /* Adjust the base font size */
       font-family: Arial, sans-serif; /* Optional: Change font family */
   }
    .search-box { margin: 20px; }
    select { width: 250px; padding: 10px; font-size: 16px; }
    option { font-size: 16px; }
    .dropdown { margin-bottom: 20px; }
</style>
<h1>Estimates in the causal regime</h1>
<p> The following tables present empirical parameter estimates for the model in the causal regime, where the mfOU process is assumed to depend solely on past realizations of the driving white noise. This assumption is incorporated by constraining the value of eta as a function of rho, H1, and H2 when calculating the theoretical cross-covariances in the minimum distance estimation. The necessity of using this model arises in the analysis of spillovers in Section 7.</p>
"""
tUniv5 = pd.read_csv("files_online_appendix/table_exa_caus_univ.csv").round(3)
mRho5 = pd.read_csv("files_online_appendix/matrix_exa_caus_rho.csv").round(3)
mEta5 = pd.read_csv("files_online_appendix/matrix_exa_caus_eta.csv").round(3)
mRho5.index = mRho5.columns
mEta5.index = mEta5.columns
for i in range(len(mRho4.columns)):
    mRho5.iloc[:i, i] = np.nan
    mEta5.iloc[:i, i] = np.nan

html_content_page[5] +="""
<h2>Univariate estimates</h2>
"""
html_content_page[5] += tUniv5.to_html(index=False, na_rep='')
html_content_page[5] +="""
<br>
<br>
<h2>Matrix RHO</h2>
"""
html_content_page[5] += mRho5.to_html(index=True, na_rep='')
html_content_page[5] +="""
<br>
<br>
<h2>Matrix ETA</h2>
"""
html_content_page[5] += mEta5.to_html(index=True, na_rep='')

# %% 6: Goodness of fit Causal
html_content_page[6] += """
<!DOCTYPE html>
<html>

<head>
    <style>
    body {
           font-size: 18px; /* Adjust the base font size */
           font-family: Arial, sans-serif; /* Optional: Change font family */
       }
        .search-box { margin: 20px; }
        select { width: 250px; padding: 10px; font-size: 16px; }
        option { font-size: 16px; }
        .dropdown { margin-bottom: 20px; }
    </style>
</head>
<body>

<h1>Goodness of covariance fit (causal regime)</h1>
<p> The following plots display the empirical auto and cross-covariances (represented by bars) of realized volatilities from the Oxford-Man dataset, alongside the causal mfOU-implied theoretical ones (depicted by red curves). The theoretical auto and cross-covariances (in the causal regime) are calculated using parameters obtained through minimum distance estimation (MDE), which targets the distance between empirical and theoretical quantities shown in the plots. </p>

<!-- Index Dropdown -->
<div class="dropdown">
    <label for="indexDropdown">Autocovariance:</label>
    <select id="indexDropdown" onchange="scrollToPlot('index')">
        <option value="">Select an index</option>
"""

# Adding options for indices dropdown
for s1 in indices:
    html_content_page[6] += f'<option value="{s1}">{s1}</option>'

html_content_page[6] += "</select></div>"

# Pairs Dropdown
html_content_page[6] += """
<div class="dropdown">
    <label for="pairDropdown">Cross-covariance:</label>
    <select id="pairDropdown" onchange="scrollToPlot('pair')">
        <option value="">Select a pair</option>
"""

# Adding options for pairs dropdown
for pair in pairs:
    s1, s2 = pair.split('/')
    s12 = s1 + "_" + s2  # This creates a unique ID like 'AEX_AORD' for 'AEX/AORD'
    html_content_page[6] += f'<option value="{s12}">{pair}</option>'

html_content_page[6] += "</select></div>"

# Add plots for each index and pair
for s1 in indices:    
    html_content_page[6] += f"""
    <div id="{s1}" style="width:1000px; display: flex; justify-content: space-between; gap: 0px; margin: 0; padding: 0;">
        <figure class="left" style="margin-right: -3px;">
            <img src="files_online_appendix/acfc_{s1}.png" width="500" height="500"/>
        </figure>
    </div>
    """

for pair in pairs:
    s1, s2 = pair.split('/')
    s12 = s1 + "_" + s2  # Unique ID like 'AEX_AORD' for 'AEX/AORD'
    
    html_content_page[6] += f"""
    <div id="{s12}" style="width:1000px; display: flex; justify-content: space-between; gap: 0px; margin: -20px 0 0 0; padding: 0;">
        <figure class="left" style="float:left">
            <img src="files_online_appendix/ccfc_{s12}.png" width="1000" height="500"/>
        </figure>
    </div>
    """

# JavaScript for scrolling to selected plots
html_content_page[6] += """
<script>
    function scrollToPlot(type) {
        let dropdown = document.getElementById(type === 'index' ? 'indexDropdown' : 'pairDropdown');
        let value = dropdown.value;
        if (value) {
            let plot = document.getElementById(value);
            plot.scrollIntoView({ behavior: 'smooth' });
        }
    }
</script>

</body>
</html>
"""

# %% 7: Compile
with open(pages[0], 'w') as f:
    f.write(html_content_page[0])

for i in range(1, len(pages)):
    html_content_page[i] += f"""
        <!-- Navigation back to the index on Page 0 -->
        <div>
            <a href="page0_ind.html">Back to Index</a>
        </div>
    </body>
    </html>
    """
    
    with open(pages[i], 'w') as f:
        f.write(html_content_page[i])

