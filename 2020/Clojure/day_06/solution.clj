(ns day_06.solution
  (:require [clojure.string :as str]
            [main :as main :refer [defoverload]]))

(def day "06")

(defn get-lines
  "Read in and parse inputs as seq of vectors."
  [file]
  (->> file
       slurp
       (#(str/split % #"\n\n"))
       (map #(str/split % #"\n"))))

(defn part1
  [_]
  (let [inputs (get-lines "day_06/inputs.txt")]
    (->> inputs
         (map #(->> (mapv seq %)
                    flatten
                    distinct
                    count))
         (reduce +))))

(defn part2
  [_]
  (letfn [(char-rize [coll]
            (->> coll
                 (map #(->> (mapv seq %)
                            flatten))))]
    (let [inputs (get-lines "day_06/inputs.txt")
          ;; note zipmap here can swallow your duplicate keys!!! e.g.
          ;; ({a 1, b 1, c 1} {a 1, b 1, c 1} {a 2, b 1, c 1} {a 4} {b 1})
          ;; (1 3 2 4 1)
          ;; zipmap will swallow and return
          ;; {{a 1, b 1, c 1} 3, {a 2, b 1, c 1} 2, {a 4} 4, {b 1} 1}
          freq->lens (map #(conj [] %1 %2)
                          (map frequencies (char-rize inputs))
                          (map count inputs))
          keeped (for [[freq len] freq->lens]
                   (filter (fn [[_ cnt]]
                             (when (= cnt len) true)) freq))]
      (->> keeped
           (map count)
           (reduce +)))))

(defoverload main/part1 day part1)
(defoverload main/part2 day part2)
