# Repo for doing Spatial Filtering Experiments

## Image Quality Metrics

| PSNR Value(db) | Image Quality |
|----------------|---------------|
| 20-25          | Poor          |
| 25-30          | Fair          |
| 30-35          | Good          |
| 35-40          | Very Good     |
| 40-45          | Excellent     |
| 45-50          | Outstanding   |


## Results

### Original Image

<details>
    <summary>Click to see original image</summary>
    <img src="results/original_image.png" alt="Original Image">
</details>



### Gaussian Noise

<details>
    <summary>Click to see Gaussian Noise</summary>
    <img src="results/gaussian_noise.png" alt="Gaussian Noise">

    PSNR Value: 20.58368544669303
</details>


### Average Filter
<details>
  <summary>Click to see Average Filter</summary>
  <div style="display: flex; flex-wrap: wrap;">
    <div style="flex: 0 0 48%; margin-right: 2%;">
      <img src="results/average3.png" alt="Average Filter 3" style="width: 100%;">
      <p>PSNR Value: 26.33309099007021</p>
    </div>
    <div style="flex: 0 0 48%;">
      <img src="results/average5.png" alt="Average Filter 5" style="width: 100%;">
      <p>PSNR Value: 24.310281233950995</p>
    </div>
    <div style="flex: 0 0 48%; margin-right: 2%;">
      <img src="results/average7.png" alt="Average Filter 7" style="width: 100%;">
      <p>PSNR Value: 22.732591750197635</p>
    </div>
    <div style="flex: 0 0 48%;">
      <img src="results/average9.png" alt="Average Filter 9" style="width: 100%;">
      <p>PSNR Value: 21.6794322779748</p>
    </div>
    <div style="flex: 0 0 48%; margin-right: 2%;">
      <img src="results/average11.png" alt="Average Filter 11" style="width: 100%;">
      <p>PSNR Value: 20.936952533749707</p>
    </div>
    <div style="flex: 0 0 48%;">
      <img src="results/average13.png" alt="Average Filter 13" style="width: 100%;">
      <p>PSNR Value: 20.38232158818918</p>
    </div>
    <div style="flex: 0 0 48%; margin-right: 2%;">
      <img src="results/average15.png" alt="Average Filter 15" style="width: 100%;">
      <p>PSNR Value: 19.940615859021648</p>
    </div>
  </div>
</details>



| Kernel Size | PSNR Value |
|----------------|---------------|
| 3          | 26.33309099007021 |
| 5          | 24.310281233950995 |
| 7          | 22.732591750197635 |
| 9          | 21.6794322779748 |
| 11         | 20.936952533749707 |
| 13         | 20.38232158818918 |
| 15         | 19.940615859021648 |

### Gaussian Filter
<details>
  <summary>Click to see Gaussian Filter</summary>
  <div style="display: flex; flex-wrap: wrap;">
    <div style="flex: 0 0 48%; margin-right: 2%;">
      <img src="results/gaussian3.png" alt="Gaussian Filter 3" style="width: 100%;">
      <p>PSNR Value: 26.76677174127444</p>
    </div>
    <div style="flex: 0 0 48%;">
      <img src="results/gaussian5.png" alt="Gaussian Filter 5" style="width: 100%;">
      <p>PSNR Value: 26.42952276805162</p>
    </div>
    <div style="flex: 0 0 48%; margin-right: 2%;">
      <img src="results/gaussian7.png" alt="Gaussian Filter 7" style="width: 100%;">
      <p>PSNR Value: 25.206562850970506</p>
    </div>
    <div style="flex: 0 0 48%;">
      <img src="results/gaussian9.png" alt="Gaussian Filter 9" style="width: 100%;">
      <p>PSNR Value: 24.36226725280244</p>
    </div>
    <div style="flex: 0 0 48%; margin-right: 2%;">
      <img src="results/gaussian11.png" alt="Gaussian Filter 11" style="width: 100%;">
      <p>PSNR Value: 23.609264920207846</p>
    </div>
    <div style="flex: 0 0 48%;">
      <img src="results/gaussian13.png" alt="Gaussian Filter 13" style="width: 100%;">
      <p>PSNR Value: 22.970936336497342</p>
    </div>
    <div style="flex: 0 0 48%; margin-right: 2%;">
      <img src="results/gaussian15.png" alt="Gaussian Filter 15" style="width: 100%;">
      <p>PSNR Value: 22.44196861753025</p>
    </div>
  </div>
</details>


| Kernel Size | PSNR Value |
|----------------|---------------|
| 3          | 26.76677174127444 |
| 5          | 26.42952276805162 |
| 7          | 25.206562850970506 |
| 9          | 24.36226725280244 |
| 11         | 23.609264920207846 |
| 13         | 22.970936336497342 |
| 15         | 22.44196861753025 |


### Laplacian Filter and Discontinuity Map

<details>
  <summary>Click to see Laplacian Filter and respective Discontinuity Map</summary>
  <div style="display: flex; justify-content: space-between;">
    <div style="flex: 0 0 48%;">
      <img src="results/laplacian1.png" alt="Laplacian Filter 1" style="width: 100%;">
    </div>
    <div style="flex: 0 0 48%;">
      <img src="results/laplacian1_dis.png" alt="Discontinuity Map 1" style="width: 100%;">
      <p>PSNR Value: 7.642565281014162</p>
    </div>
  </div>
  <div style="display: flex; justify-content: space-between;">
    <div style="flex: 0 0 48%;">
      <img src="results/laplacian2.png" alt="Laplacian Filter 2" style="width: 100%;">
    </div>
    <div style="flex: 0 0 48%;">
      <img src="results/laplacian2_dis.png" alt="Discontinuity Map 2" style="width: 100%;">
      <p>PSNR Value: 6.432201648386924</p>
    </div>
  </div>
  <div style="display: flex; justify-content: space-between;">
    <div style="flex: 0 0 48%;">
      <img src="results/laplacian3.png" alt="Laplacian Filter 3" style="width: 100%;">
    </div>
    <div style="flex: 0 0 48%;">
      <img src="results/laplacian3_dis.png" alt="Discontinuity Map 3" style="width: 100%;">
      <p>PSNR Value: 7.4557307035857345</p>
    </div>
  </div>
  <div style="display: flex; justify-content: space-between;">
    <div style="flex: 0 0 48%;">
      <img src="results/laplacian4.png" alt="Laplacian Filter 4" style="width: 100%;">
    </div>
    <div style="flex: 0 0 48%;">
      <img src="results/laplacian4_dis.png" alt="Discontinuity Map 4" style="width: 100%;">
      <p>PSNR Value: 9.239515678118183</p>
    </div>
  </div>
</details>



| Filter Type | PSNR Value |
|----------------|---------------|
| 1          | 7.642565281014162 |
| 2          | 6.432201648386924 |
| 3          | 7.4557307035857345 |
| 4          | 9.239515678118183 |
