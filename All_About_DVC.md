# DVC (Data Version Control)

DVC is a tool used to version control large files, datasets, and machine learning models—something that traditional version control systems struggle with.

DVC helps to:

* Track datasets
* Manage data pipelines
* Reproduce experiments

Instead of storing large files directly in Git, DVC stores metadata (`.dvc` files) in Git and keeps the actual data in remote storage such as S3, Google Drive, or a local database.

While Git is used for tracking code changes, collaboration, and version history of files, DVC focuses on data and models.

---

## Difference Between DVC and Git

| Feature             | Git                      | DVC                                    |
| ------------------- | ------------------------ | -------------------------------------- |
| Purpose             | Version control for code | Version control for data and ML models |
| Handle Large Files  | Poor                     | Efficient                              |
| Stores Data         | In repository            | External storage                       |
| Track Changes       | Code changes             | Data and model changes                 |
| Pipeline Management | No                       | Yes                                    |
| Reproducibility     | Limited                  | Strong support                         |
| Works with ML       | Not designed             | Designed for ML                        |

---

## Important Commands

1. `dvc init`
   Initializes DVC in your project. It creates a `.dvc` folder and configuration files. It must be run after `git init`.

2. `dvc add <file>`
   Creates a `.dvc` file, adds the original file to `.gitignore`, and stores the file in DVC cache.

3. ```
   git add data.dvc .gitignore  
   git commit -m "track dataset"
   ```

   Git tracks metadata, not the actual data.

4. `dvc remote add -d <name> <path>`
   Connects remote storage like S3, Google Drive, or local storage. `-d` sets it as default remote.

5. `dvc push`
   Uploads data to remote storage.

6. `dvc pull`
   Downloads data from remote storage.

7. `dvc checkout`
   Restores data version based on Git commit and syncs workspace with `.dvc` files.

8. `dvc remove <file>`
   Stops tracking a file.

---

## Run Pipeline Stage

9. ```
    dvc stage add -n preprocess -d preprocess.py -d data.csv -o cleaned.csv python preprocess.py
    ```

* `-n` : stage name
* `-d` : dependencies
* `-o` : outputs

10. `dvc repro`
    Reruns pipeline when data or code changes.

11. `dvc dag`
    Visualizes the pipeline.

---

## Interview Questions

### 1. Why do we need DVC if we already have Git?

Git is very good for tracking code, but it is not designed to handle large files like datasets or machine learning models.

DVC helps us:

* Track large data files and models
* Keep version history of data like Git does for code
* Store heavy files outside Git (cloud or local storage)

**In short:**
Git = code versioning
DVC = data and model versioning

---

### 2. What files does DVC create?

* `dvc.yaml` → stores pipeline stages
* `dvc.lock` → keeps exact versions for reproducibility
* `.dvc` files → track individual data files or folders
* `.dvc/` folder → contains DVC internal settings and cache

---

### 3. What is DVC Cache?

DVC cache is a storage area where DVC keeps copies of data files.

* Stores data using hash values (unique IDs)
* Avoids storing duplicate files
* Saves space and improves speed

**In simple words:**
DVC cache is a smart storage system that avoids duplicate data and speeds up tracking.
