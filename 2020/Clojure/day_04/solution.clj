(ns day_04.solution
  (:require [clojure.string :as str]
            [clojure.spec.alpha :as spec]
            [main :as main :refer [defoverload]]))

(def day "04")

(defn get-lines
  "Read in and parse inputs as seq of vectors."
  [file]
  (letfn [(add-to-map [m s]
            (let [[k v] (str/split s #":")]
              (assoc m k v)))]
    (->> file
         slurp
         ;; split by new lines followed by blank lines
         (#(str/split % #"\n\n"))
         ;; split by new lines or spaces
         (map #(str/split % #"\n| "))
         ;; reduce to covert colon pairs to maps
         (map #(reduce add-to-map {} %)))))

(defn validate-passports
  "Validate inputs by comparing mandatory and optional keys."
  [inputs]
  (let [mandatory-keys #{"ecl" "pid" "eyr" "hcl" "byr" "iyr" "hgt"}
        optional-keys #{"cid"}]
    (->> inputs
         (map #(when (every? (set (keys %)) mandatory-keys) true))
         ;; note `keep` won't work here since it only removes nils!
         (filter true?)
         count)))

(defn validate-passports-advanced
  "Validate inputs with advanced criteria."
  [inputs]
  (let [mandatory-keys #{"ecl" "pid" "eyr" "hcl" "byr" "iyr" "hgt"}
        optional-keys #{"cid"}]
    (letfn [(valid? [m]
              (when (and
                      ;; contains all mandatory keys
                      (every? (set (keys m)) mandatory-keys)
                      ;; byr (Birth Year) - four digits; at least 1920 and at most 2002
                      (let [byr (m "byr")]
                        (and (= (count byr) 4)
                             (spec/int-in-range? 1920 2003 (read-string byr))))
                      ;; iyr (Issue Year) - four digits; at least 2010 and at most 2020.
                      (let [iyr (m "iyr")]
                        (and
                          (= (count iyr) 4)
                          (spec/int-in-range? 2010 2021 (read-string iyr))))
                      ;; eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
                      (let [eyr (m "eyr")]
                        (and
                          (= (count eyr) 4)
                          (spec/int-in-range? 2020 2031 (read-string eyr))))
                      ;; hgt (Height) - a number followed by either cm or in:
                      (let [hgt (m "hgt")]
                        (or
                          ;; If cm, the number must be at least 150 and at most 193.
                          (and
                              (str/ends-with? hgt "cm")
                              (-> hgt
                                  (str/split #"cm")
                                  first
                                  read-string
                                  (->> (spec/int-in-range? 150 194))))
                          ;; If in, the number must be at least 59 and at most 76.
                            (and
                              (str/ends-with? hgt "in")
                              (-> hgt
                                  (str/split #"in")
                                  first
                                  read-string
                                  (->> (spec/int-in-range? 59 77)))
                              )))
                      ;; hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
                      (let [hcl (m "hcl")]
                        (and
                          (str/starts-with? hcl "#")
                          (-> hcl
                              (str/split #"#")
                              second
                              (#(re-matches #"([0-9]|[a-f]){6}" %)))))
                      ;; ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
                      ((set (map str '[amb blu brn gry grn hzl oth])) (m "ecl"))
                      ;; pid (Passport ID) - a nine-digit number, including leading zeroes.
                      (= (count (m "pid")) 9)
                      )
                true))]
      (->> inputs
           (map valid?)
           ;; note `keep` won't work here since it only removes nils!
           (filter true?)
           count))))

(defn part1
  [_]
  (let [inputs (get-lines "day_04/inputs.txt")]
    (validate-passports inputs)))

(defn part2
  [_]
  (let [inputs (get-lines "day_04/inputs.txt")]
    (validate-passports-advanced inputs)))

(defoverload main/part1 day part1)
(defoverload main/part2 day part2)
